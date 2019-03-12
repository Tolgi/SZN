"""Да се напише функција која ќе генерира табела на слични корисници претставена како речник од речници
 (клучеви се имињата на корисниците), така што за секој пар корисници ќе чува торка од сличност базирана
 на Пеарсонова корелација, сличност базирана на Евклидово растојание, и број на заеднички оцени
 (оцени дадени за исти филмови). Вредностите да бидат заокружени на 3 децимали. За прочитани имиња на двајца
 корисници да се испечати торката која се чува во генерираната табела."""
oceniPoKorisnici={
    'Lisa Rose': {'Catch Me If You Can': 3.0 , 'Snakes on a Plane': 3.5, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0, 'Snitch': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,  'The Night Listener': 3.0,'You, Me and Dupree': 3.5},
    'Michael Phillips': {'Catch Me If You Can': 2.5, 'Lady in the Water': 2.5,'Superman Returns': 3.5, 'The Night Listener': 4.0, 'Snitch': 2.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,'The Night Listener': 4.5, 'Superman Returns': 4.0,'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'Just My Luck': 2.0, 'Superman Returns': 3.0, 'You, Me and Dupree': 2.0},
    'Jack Matthews': {'Catch Me If You Can': 4.5, 'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'Snitch': 4.5},
    'Toby': {'Snakes on a Plane':4.5, 'Snitch': 5.0},
    'Michelle Nichols': {'Just My Luck' : 1.0, 'The Night Listener': 4.5, 'You, Me and Dupree': 3.5, 'Catch Me If You Can': 2.5, 'Snakes on a Plane': 3.0},
    'Gary Coleman': {'Lady in the Water': 1.0, 'Catch Me If You Can': 1.5, 'Superman Returns': 1.5, 'You, Me and Dupree': 2.0},
    'Larry': {'Lady in the Water': 3.0, 'Just My Luck': 3.5, 'Snitch': 1.5, 'The Night Listener': 3.5}
    }

from math import sqrt
def sim_n(oceni, person1, person2):
    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())

    zaednicki = filmovi1.intersection(filmovi2)
    n = len(zaednicki)
    if n == 0: return 0

    return n


def sim_distance(oceni, person1, person2):

    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())

    zaednicki = filmovi1.intersection(filmovi2)
    n = len(zaednicki)
    if n == 0: return 0

    suma = 0.0
    for item in zaednicki:
        ocena1 = oceni[person1][item]
        ocena2 = oceni[person2][item]

        suma += (ocena1-ocena2)**2

    rezultat = 1 / (1 + sqrt(suma))
    return  round(rezultat,3)

def sim_pearson(oceni, person1, person2):

    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())

    zaednicki = filmovi1.intersection(filmovi2)
    n = len(zaednicki)
    if n == 0: return 0
    sumx = 0
    sumy = 0
    sumxSq = 0
    sumySq = 0
    psum = 0

    for item in zaednicki:
        ocena1 = oceni[person1][item]
        ocena2 = oceni[person2][item]

        sumx += ocena1
        sumxSq += ocena1 ** 2
        sumy += ocena2
        sumySq += ocena2 ** 2
        psum += ocena1 * ocena2

    de = psum - ((sumx * sumy) / n)
    deli = sqrt(sumxSq - (pow(sumx,2) / n)) * sqrt(sumySq - (pow(sumy,2) / n))

    if de==0: return 0
    rezultat = de / deli
    return  round(rezultat,3)

def my_func(oceni):
    rezultat = {}

    for person1 in oceni.keys():
        for person2 in oceni.keys():
            if person1 == person2: continue
            simPearson = sim_pearson(oceni, person1, person2)
            simDistance = sim_distance(oceni, person1, person2)
            n = sim_n(oceni, person1, person2)
            rezultat.setdefault(person1,{})
            rezultat[person1][person2] = simDistance, simPearson, n

    return rezultat


if __name__ == "__main__":
    korisnik1 = input()
    korisnik2 = input()
    # korisnik1='Mick LaSalle'
    # korisnik2='Lisa Rose'
    # print oceniPoKorisnici
    tabela = my_func(oceniPoKorisnici)
    # print tabela
    print(tabela[korisnik1][korisnik2])