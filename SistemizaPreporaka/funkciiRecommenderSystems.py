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
"""---------------------------------Slicnost spored Evklidovo rastojanie ---------------------------------"""

def slicnostEvklidovo(oceni, person1, person2):

    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())

    zadenicki = filmovi1.intersection(filmovi2)
    if len(zadenicki) == 0: return 0

    suma = 0.0
    for item in zadenicki:
        ocena1 = oceni[person1][item]
        ocena2 = oceni[person2][item]

        suma += (ocena1 - ocena2) ** 2

    return 1 / (1 + sqrt(suma))

#print(slicnostEvklidovo(critics, 'Jack Matthews', 'Gary Coleman'))
#print(slicnostEvklidovo(critics, 'Jack Matthews', 'Michelle Nichols'))


"""--------------------------------Slicnost spored Pearsonova korelacija------------------------------------------"""

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

#print("Razlika pomegu SlicnostParsonovo vs SlicnostEvklidovo: ")
#print(slicnostPearsonova(critics, 'Jack Matthews', 'Gary Coleman'), slicnostEvklidovo(critics, 'Jack Matthews', 'Gary Coleman'))
#print(slicnostPearsonova(critics, 'Jack Matthews', 'Michelle Nichols'), slicnostEvklidovo(critics, 'Jack Matthews', 'Michelle Nichols'))
#print(slicnostPearsonova(movies, 'Catch Me If You Can', 'Lady in the Water'), slicnostEvklidovo(movies, 'Catch Me If You Can', 'Lady in the Water'))


"""-----------------------------Gi vrakja najslicnite n korisnici na daden korisnik----------------------------"""

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

#print()
#print("TOP slicni se: ")
#print(topSlicni(critics, 'Michael Phillips', 100, slicnostEvklidovo))
#print(topSlicni(critics, 'Michael Phillips', 100))

"""----------------------Dobivanje preporaki od slicnite korisnici za daden korisnik--------------------------------"""

"""za sekoj item (film) koj sto korisnikot go nema rangirano/gledano se presmetuva zbir od tezinskite rejtinzi 
   (tezinski rejting = slicnosta koja ja ima toj korisnik so dadeniot * ocenata koja ja ima dadeno)
   
   za sekoj item (film) koj sto korisnikot go nema rangirani/gledano se presmetuva zbir od slicnosta na kriticarite koi
   go imaat oceneto filmot"""


def zemiPreporaki(oceni, person, slicnost=slicnostPearsonova, min_zaednicki=None):
    totals = {}
    sliSums = {}
    for person2 in oceni.keys():
        if person == person2: continue
        filmovi1=set(oceni[person].keys())
        filmovi2=set(oceni[person2].keys())
        zaednicki = filmovi1.intersection(filmovi2)

        if min_zaednicki and len(zaednicki) < min_zaednicki:
            print("So korisnikot", person2, "imame samo: ", len(zaednicki), "pa go prekoknuvame!")
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

print(zemiPreporaki(critics, 'Michael Phillips'))
print(zemiPreporaki(critics, 'Michael Phillips', min_zaednicki=3))

"""-------------------------------Transformiraj recnik / Invertiranje na mnozesto------------------------"""
def invertirajMnozestvo(oceni):
    rezultat={}
    for person in oceni.keys():
        for item in person:
            rezultat.setdefault(item,0)
            rezultat[item][person] = oceni[person][item]

    return rezultat

"""------------------------------------------------------------"""









