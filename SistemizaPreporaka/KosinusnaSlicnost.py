"""Да испрограмира функција за косинусна сличност која е дефинирана со следнава формула, каде A е листа со
оцените на едниот корисник или филм, а B е листа со оцените на другиот корисник или филм:
http://code.finki.ukim.mk/public/uploads/1453390764510.png
     similarity=cos(teta)=(A*b/||A|| ||B||)=(Suma(i do n)Ai*Bi)/sqrt(Suma(i do n)(Ai^2)*sqrt(Suma(i do n)(Bi^2))
Притоа треба да се избегне делење со нула и во тој случај да се смета дека сличноста е -1.
Речник со оцени на корисници по филмови треба е веќе даден. Од стандардниот влез се вчитува име на еден
филм. Да се испечати сличноста на прочитаниот филм со секој друг филм (освен самиот со себе) така што ќе
се печати:
Филм 2
Косинусна сличност, Пеарсонова сличност, Евклидова сличност
Празна линија

При печатењето филмовите треба да бидат подредени по азбучен редослед. Сите сличности треба да бидат
заокружени на 2 децимали.
Vlez:
'Catch Me If You Can'
IZlez:
Just My Luck
1.0 0 0.4
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

from math import sqrt
def transformoceni(oceni):
    result = {}
    for person in oceni.keys():
        for item in oceni[person]:
            result.setdefault(item, {})
            # Zameni gi mestata na licnosta i predmetot
            result[item][person] = oceni[person][item]
    return result

# Vrakja merka za slicnost bazirana na rastojanieto za person1 i person2
def sim_distance(oceni, person1, person2):
    # Se pravi lista na zaednicki predmeti (filmovi)

    filmovi1=set(oceni[person1].keys())
    filmovi2=set(oceni[person2].keys())
    zaednicki = filmovi1.intersection(filmovi2)
#     print(filmovi1)
#     print(filmovi2)
#     print(zaednicki)
#     for item in oceni[person1].keys():
#         if item in oceni[person2]:
#             zaednicki.add(item)
#     # ako nemaat zaednicki rejtinzi, vrati 0
    if len(zaednicki) == 0: return 0
#     # Soberi gi kvadratite na zaednickite razliki
    suma = 0.0
    for item in zaednicki:
        ocena1 = oceni[person1][item]
        ocena2 = oceni[person2][item]
        suma += (ocena1 - ocena2) ** 2
#         print(item, person1, ocena1, person2, ocena2)

    return round((1 / (1 + sqrt(suma))),2)

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
    return round(r,2)


def sim_cosinus(oceni, person1, person2):

    filmovi1 = set(oceni[person1].keys())
    filmovi2 = set(oceni[person2].keys())
    zaednicki = filmovi1.intersection(filmovi2)

    if len(zaednicki) == 0: return 0

    sumA = 0
    sumB = 0
    psum = 0

    for i in zaednicki:
        ocena1 = oceni[person1][i]
        ocena2 = oceni[person2][i]
        sumA += ocena1**2
        sumB += ocena2**2
        psum += ocena1*ocena2

    den = sqrt(sumA) * sqrt(sumB)
    if den == 0: r = -1
    else:
        r = psum / den
    return round(r,2)


if __name__ == "__main__":
    film = input()
    oceniPoFilm = transformoceni(critics)

    for film2 in oceniPoFilm.keys():
        if film2 == film: continue
        else:
            kosinusna = sim_cosinus(oceniPoFilm, film, film2)
            pearson = sim_pearson(oceniPoFilm, film, film2)
            distance = sim_distance(oceniPoFilm, film, film2)
            print(film2)
            print(kosinusna," ",pearson," ",distance)
            print()




