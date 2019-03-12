"""За корисникот внесен на влез да се препорача филм. Да се користи Пирсонов коефициент на корелација
како мерка. Ако корисникот го нема во базата да се препорача најгледаниот филм. Доколку корисникот има
гледано повеќе од 5 филмови, да се препорача според филмовите, во спротивно да се препорача според
корисниците кои се слични со него."""
from math import sqrt

critics = {
    'Lisa Rose': {'Catch Me If You Can': 3.0, 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5,
                  'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5, 'The Night Listener': 3.0,
                     'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5, 'Superman Returns': 3.5,
                         'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0,
                     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0,
                     'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane': 4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck': 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5,
                         'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5,
                     'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
}

def korisnikVoBaza(person, oceni):

    flag = 0;
    for p in oceni.keys():
        if p == person: flag = 1

    if flag == 1: return person
    else: return 0

def najgledanFilm(filmovi):

    max = 0
    najgledan = " "
    for f in filmovi.keys():
        n = len(filmovi[f].keys())
        #print("Filmot ", f, "e gledan: ", n)
        if n > max:
            max = n
            najgledan = f
    return  najgledan

def invertirajMnozestvo(oceni):
    rezultat={}
    for person in oceni.keys():
        for item in oceni[person]:
            rezultat.setdefault(item,{})
            rezultat[item][person] = oceni[person][item]

    return rezultat

def slicnostPearsonova (oceni, person1, person2):

    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())

    zaednicki = filmovi1.intersection(filmovi2)
    n = len(zaednicki)
    if n == 0: return 0

    #sumi od ocenkite za sekoja licnost posebno
    sum1 = 0.0
    sum2 = 0.0
    #sumi od kvadratite na ocenkite za sekoja licnost posebno
    sum1sq = 0.0
    sum2sq = 0.0
    #suma od proizvodot na ocenkite od person1 i person2
    psum = 0.0

    for item in zaednicki:
        ocena1 = oceni[person1][item]
        ocena2 = oceni[person2][item]

        sum1 += ocena1
        sum1sq += ocena1 ** 2
        sum2 += ocena2
        sum2sq += ocena2 ** 2

        psum += ocena1 * ocena2
    dl = psum - (sum1 * sum2 / n)
    de = sqrt(sum1sq - pow(sum1, 2) / n) * sqrt(sum2sq - pow(sum2, 2) / n)
    if de == 0: return  0

    r = dl / de
    return  r

def topSlicni(oceni, person, n=5, slicnost = slicnostPearsonova):


    scores = []
    for person2 in oceni.keys():
        if person2 != person:
            s = slicnost(oceni, person, person2)
            scores.append((s, person2))

    scores.sort()
    scores.reverse()

    if n is None:
        return scores
    else:
        return scores[0:n]

def zemiPreporaki(oceni, person, slicnost=slicnostPearsonova, min_zaednicki=None):
    totals = {}
    sliSums = {}
    for person2 in oceni.keys():
        if person == person2: continue
        filmovi1=set(oceni[person].keys())
        filmovi2=set(oceni[person2].keys())
        zaednicki = filmovi1.intersection(filmovi2)

        if min_zaednicki and len(zaednicki) < min_zaednicki:
           # print("So korisnikot", person2, "imame samo: ", len(zaednicki), "pa go prekoknuvame!")
            continue

        sli = slicnost(oceni,person,person2)
        if sli <= 0: continue

        for item in oceni[person2].keys():
            if item not in oceni[person]:
                totals.setdefault(item, 0)
                totals[item] += oceni[person2][item] * sli
                sliSums.setdefault(item, 0)
                sliSums[item] += sli

    preporaki = []
    for item, score in totals.items():
        sli_total = sliSums[item]
        final_score = round(score / sli_total, 1)
        preporaki.append((final_score, item))

    preporaki.sort(reverse=True)
    #preporaki.reverse()
    return preporaki

def item_based(critics, person1, n=3):
    oceni_po_film = invertirajMnozestvo(critics)
    similarity_per_item = {}
    for item in critics[person1].keys():
        similar_items = topSlicni(oceni_po_film, item, n=None)
        my_rating = critics[person1][item]

        for similarity, item2 in similar_items:
            if item2 in critics[person1] or similarity <= 0:
#                 print('Slicnost', similarity, 'na', item,'so', item2)
                continue
            weight= similarity * my_rating
#             print('Slicnost', similarity, 'na', item,'so', item2, weight)
            similarity_per_item.setdefault(item2, [])
            similarity_per_item[item2].append(weight)
#         print(item, my_rating, list(similarity_per_item.items()))
    similarity_per_item_avg = []
    import numpy as np
    for item in similarity_per_item:
      #  print(item, similarity_per_item[item])
        avg_sim = np.mean(similarity_per_item[item])
        similarity_per_item_avg.append((avg_sim, item))
    similarity_per_item_avg.sort(reverse=True)
    return similarity_per_item_avg[:n]


if __name__ == "__main__":
    korisnik = input()
    recnikFilmovi = invertirajMnozestvo(critics)
    if korisnik not in critics:
       print(najgledanFilm(recnikFilmovi))
    else:
        n = len(critics[korisnik].keys())
        if n < 5:
            preporaki = zemiPreporaki(critics, korisnik)
            print("POMALI OD 5")
            print(preporaki)
        else:
            preporaki = item_based(critics, korisnik)
            print("POGOLEMI OD 5")
            print(preporaki)

