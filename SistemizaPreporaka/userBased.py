
"""По изработка на задачите од претходната вежба веќе ќе имате две тренинг множества претставени во Python
како речник од речници. Искористете ги за изработка на систем за препораки така што да може на
секој од тест корисниците да им предложи по 3 филмови, еднаш користејќи item-based, а еднаш user-based
препораки. При item-based пристапот се предлагаат фимови кои ги нема гледано корисникот кои се со
позитивна сличност со некои од филмовите кои ги има гледано.
На излез треба да се печатат две листи кои ги содржат само имињата на предложените филмови во растечки
(азбучен) редослед. Првата листа е според user-based, а втората според item-based пристап.

Input: 'Gary Coleman'
Output:
user-based: ['Snakes on a Plane', 'Snitch', 'The Night Listener']
item-based: ['Just My Luck', 'Snakes on a Plane', 'Snitch']
 """

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

movies = {
    'Lady in the Water': {'Gary Coleman': 1.0, 'Larry': 3.0, 'Jack Matthews': 3.0, 'Michael Phillips': 2.5,
                          'Gene Seymour': 3.0, 'Mick LaSalle': 3.0, 'Michelle Nichols': 3.0},
    'Snakes on a Plane': {'Jack Matthews': 4.0, 'Mick LaSalle': 4.0, 'Claudia Puig': 3.5, 'Lisa Rose': 3.5, 'Toby': 4.5,
                          'Gene Seymour': 3.5},
    'Just My Luck': {'Larry': 3.5, 'Claudia Puig': 3.0, 'Gene Seymour': 1.5, 'Mick LaSalle': 2.0,
                     'Michelle Nichols': 1.0},
    'Superman Returns': {'Gary Coleman': 1.5, 'Jack Matthews': 5.0, 'Mick LaSalle': 3.0, 'Claudia Puig': 4.0,
                         'Lisa Rose': 3.5, 'Michael Phillips': 3.5},
    'The Night Listener': {'Larry': 3.5, 'Jack Matthews': 3.0, 'Claudia Puig': 4.5, 'Lisa Rose': 3.0,
                           'Gene Seymour': 3.0, 'Michael Phillips': 4.0, 'Michelle Nichols': 4.5},
    'You, Me and Dupree': {'Gary Coleman': 2.0, 'Jack Matthews': 3.5, 'Mick LaSalle': 2.0, 'Claudia Puig': 2.5,
                           'Lisa Rose': 2.5, 'Gene Seymour': 3.5, 'Michelle Nichols': 3.5},
    'Catch Me If You Can': {'Lisa Rose': 3.0, 'Michael Phillips': 2.5, 'Jack Matthews': 4.5, 'Gary Coleman': 1.5},
    'Snitch': {'Larry': 1.5, 'Toby': 5.0, 'Michael Phillips': 2.0, 'Lisa Rose': 3.0, 'Jack Matthews': 4.5}
}


from math import sqrt
# Go vrakja koeficientot na Pearsonova korelacija pomegu p1 i p2 (licnost 1 i licnost 2)
# Vrednostite se pomegu -1 i 1
def sim_pearson(oceni, p1, p2):
    # Se kreira recnik vo koj ke se cuvaat predmetite (filmovi) koi se oceneti od dvajcata
    # Vo recnikot ni se vazni samo klucevite za da gi cuvame iminjata na filmovite koi se zaednicki, a vrednostite ne ni se vazni
    zaednicki = set()
    for item in oceni[p1]:
        if item in oceni[p2]:
            zaednicki.add(item)

    # Se presmetuva brojot na predmeti oceneti od dvajcata
    n = len(zaednicki)

    # Ako nemaat zaednicki predmeti vrati korelacija 0
    if n == 0: return 0

    # Soberi gi zaednickite oceni (rejtinzi) za  sekoja licnost posebno
    sum1 = 0
    sum2 = 0

    # Soberi gi kvadratite od zaednickite oceni (rejtinzi) za  sekoja licnost posebno
    sum1Sq = 0
    sum2Sq = 0

    # Soberi gi proizvodite od ocenite na dvete licnosti
    pSum = 0
    for item in zaednicki:
        ocena1 = oceni[p1][item]
        ocena2 = oceni[p2][item]
        sum1 += ocena1
        sum1Sq += ocena1 ** 2
        sum2 += ocena2
        sum2Sq += ocena2 ** 2
        pSum += ocena1 * ocena2

    # Presmetaj go koeficientot na korelacija
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0
    r = num / den
    return r


def topMatches(oceni, person, n=5, similarity=sim_pearson):
    scores = []
    for person2 in oceni.keys():
        if person != person2:
            s = similarity(oceni, person, person2)
            if s > 0:
             scores.append((s, person2))
    # Se sortira listata vo rastecki redosled
    scores.sort()
    # Se prevrtuva za najslicnite (so najgolema vrednost) da bidat prvi
    scores.reverse()
    if n is None:
        return scores
    else:
        return scores[0:n]


def getRecommendations(oceni, person, similarity=sim_pearson, min_zaednicki=None):
    totals = {}
    simSums = {}
    for person2 in oceni.keys():
        # Za da ne se sporeduva so samiot sebe
        if person2 == person: continue
        filmovi1=set(oceni[person].keys())
        filmovi2=set(oceni[person2].keys())
        zaednicki = filmovi1.intersection(filmovi2)
        # ova e ako se bara minimum zaednicki filmovi
        # za da se zemat vo predvid ocenite na drugiot korisnik
        if min_zaednicki and len(zaednicki)<min_zaednicki:
            print('So korisnikot', person2, 'imame samo',len(zaednicki),'filmovi, pa go preskoknuvame')
            continue
        sim = similarity(oceni, person, person2)
#         print(person,person2,sim)
        # ne se zemaat vo predvid rezultati <= 0
        if sim <= 0: continue
       # print(person,person2,sim)
        for item in oceni[person2].keys():
#             print(item, oceni[person].get(item, None), oceni[person2].get(item, None))
            # za tekovniot korisnik gi zemame samo filmovite sto gi nemame veke gledano
            if item not in oceni[person]: # or oceni[person][item] == 0:
                # similarity * Score   (Slicnost * Ocena)
               # print(item, sim, oceni[person2][item], sim* oceni[person2][item])
                totals.setdefault(item, 0)
                totals[item] += oceni[person2][item] * sim

                # Sumuma na slicnosti
                simSums.setdefault(item, 0)
                simSums[item] += sim
       # print()
#     return
   # print()
    # Kreiranje na normalizirana lista so rejtinzi
    # rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings = []
    for item, weighted_score in totals.items():
        sim_total = simSums[item]
        my_score = round(weighted_score / sim_total, 1)
        #print(item, weighted_score, sim_total, my_score)
        rankings.append((my_score, item))

    # Sortiranje na listata vo rastecki redosled
    rankings.sort(reverse=True)
    # Prevrtuvanje na lista za najgolemite vrednosti da bidat napred
#     rankings.reverse()
    return rankings


def transformoceni(oceni):
    result = {}
    for person in oceni.keys():
        for item in oceni[person]:
            result.setdefault(item, {})
            # Zameni gi mestata na licnosta i predmetot
            result[item][person] = oceni[person][item]
    return result


def item_based(critics, person1, n=3):
    oceni_po_film = transformoceni(critics)
    similarity_per_item = {}
    for item in critics[person1].keys():
        similar_items = topMatches(oceni_po_film, item, n=None)
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
        #print(item, similarity_per_item[item])
        avg_sim = np.mean(similarity_per_item[item])
        similarity_per_item_avg.append((avg_sim, item))
    similarity_per_item_avg.sort(reverse=True)
    return similarity_per_item_avg[:n]


if __name__=="__main__":
    korisnik = input()
    userBased = getRecommendations(critics, korisnik)

    ub = []
    for i in userBased:
        ub.append((i[1]))

    ub = ub[:3]
    ub.sort()
    print("user-based: ",ub)

    itemBased = item_based(critics, korisnik)
    ib = []
    for i in itemBased:
        ib.append((i[1]))

    ib = ib[:3]
    ib.sort()
    print("item-based: ",ib)
