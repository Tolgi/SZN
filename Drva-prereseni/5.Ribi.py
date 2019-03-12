""""

Дадено е податочно множество од риби кое ги содржи следните видови:
    Code Finnish  Swedish    English        Latin

     1   Lahna    Braxen     Bream          Abramis brama
     2   Siika    Iiden      Whitewish      Leusiscus idus
     3   Saerki   Moerten    Roach          Leuciscus rutilus
     4   Parkki   Bjoerknan  ?              Abramis bjrkna
     5   Norssi   Norssen    Smelt          Osmerus eperlanus
     6   Hauki    Jaedda     Pike           Esox lucius
     7   Ahven    Abborre    Perch          Perca fluviatilis

Дадени се следните атрибути:
    0  Weight      Weight of the fish (in grams)
    1  Length1     Length from the nose to the beginning of the tail (in cm)
    2  Length2     Length from the nose to the notch of the tail (in cm)
    3  Length3     Length from the nose to the end of the tail (in cm)
    4  Height%     Maximal height as % of Length3
    5  Width%      Maximal width as % of Length3
Класата е дадена во последната колона.

Да се направи модел за класификација за даденото податочно множество.
За тренинг да се земат само првите 5 примероци од секоја од класите во множеството.
 Притоа ова да се направи во програмата, а не со рачно копирање! Да се класифицира елементот од податочното множество даден
 на влез и да се испечати предвидувањето. Елементот е даден со индексот од податочното множество.
---------------------------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    index = input()

    solution=None
    print solution
---------------------------------------------------------------------------------------------------------------------------------------
Sample input
15
Sample output
1
"""

data = [[242.0, 23.2, 25.4, 30.0, 38.4, 13.4, 1],
        [290.0, 24.0, 26.3, 31.2, 40.0, 13.8, 1],
        [340.0, 23.9, 26.5, 31.1, 39.8, 15.1, 1],
        [363.0, 26.3, 29.0, 33.5, 38.0, 13.3, 1],
        [430.0, 26.5, 29.0, 34.0, 36.6, 15.1, 1],
        [450.0, 26.8, 29.7, 34.7, 39.2, 14.2, 1],
        [500.0, 26.8, 29.7, 34.5, 41.1, 15.3, 1],
        [390.0, 27.6, 30.0, 35.0, 36.2, 13.4, 1],
        [450.0, 27.6, 30.0, 35.1, 39.9, 13.8, 1],
        [500.0, 28.5, 30.7, 36.2, 39.3, 13.7, 1],
        [475.0, 28.4, 31.0, 36.2, 39.4, 14.1, 1],
        [500.0, 28.7, 31.0, 36.2, 39.7, 13.3, 1],
        [500.0, 29.1, 31.5, 36.4, 37.8, 12.0, 1],
        [500.0, 29.5, 32.0, 37.3, 37.3, 13.6, 1],
        [600.0, 29.4, 32.0, 37.2, 40.2, 13.9, 1],
        [600.0, 29.4, 32.0, 37.2, 41.5, 15.0, 1],
        [700.0, 30.4, 33.0, 38.3, 38.8, 13.8, 1],
        [700.0, 30.4, 33.0, 38.5, 38.8, 13.5, 1],
        [610.0, 30.9, 33.5, 38.6, 40.5, 13.3, 1],
        [650.0, 31.0, 33.5, 38.7, 37.4, 14.8, 1],
        [575.0, 31.3, 34.0, 39.5, 38.3, 14.1, 1],
        [685.0, 31.4, 34.0, 39.2, 40.8, 13.7, 1],
        [620.0, 31.5, 34.5, 39.7, 39.1, 13.3, 1],
        [680.0, 31.8, 35.0, 40.6, 38.1, 15.1, 1],
        [700.0, 31.9, 35.0, 40.5, 40.1, 13.8, 1],
        [725.0, 31.8, 35.0, 40.9, 40.0, 14.8, 1],
        [720.0, 32.0, 35.0, 40.6, 40.3, 15.0, 1],
        [714.0, 32.7, 36.0, 41.5, 39.8, 14.1, 1],
        [850.0, 32.8, 36.0, 41.6, 40.6, 14.9, 1],
        [1000.0, 33.5, 37.0, 42.6, 44.5, 15.5, 1],
        [920.0, 35.0, 38.5, 44.1, 40.9, 14.3, 1],
        [955.0, 35.0, 38.5, 44.0, 41.1, 14.3, 1],
        [925.0, 36.2, 39.5, 45.3, 41.4, 14.9, 1],
        [975.0, 37.4, 41.0, 45.9, 40.6, 14.7, 1],
        [950.0, 38.0, 41.0, 46.5, 37.9, 13.7, 1],
        [270.0, 23.6, 26.0, 28.7, 29.2, 14.8, 2],
        [270.0, 24.1, 26.5, 29.3, 27.8, 14.5, 2],
        [306.0, 25.6, 28.0, 30.8, 28.5, 15.2, 2],
        [540.0, 28.5, 31.0, 34.0, 31.6, 19.3, 2],
        [800.0, 33.7, 36.4, 39.6, 29.7, 16.6, 2],
        [1000.0, 37.3, 40.0, 43.5, 28.4, 15.0, 2],
        [40.0, 12.9, 14.1, 16.2, 25.6, 14.0, 3],
        [69.0, 16.5, 18.2, 20.3, 26.1, 13.9, 3],
        [78.0, 17.5, 18.8, 21.2, 26.3, 13.7, 3],
        [87.0, 18.2, 19.8, 22.2, 25.3, 14.3, 3],
        [120.0, 18.6, 20.0, 22.2, 28.0, 16.1, 3],
        [0.0, 19.0, 20.5, 22.8, 28.4, 14.7, 3],
        [110.0, 19.1, 20.8, 23.1, 26.7, 14.7, 3],
        [120.0, 19.4, 21.0, 23.7, 25.8, 13.9, 3],
        [150.0, 20.4, 22.0, 24.7, 23.5, 15.2, 3],
        [145.0, 20.5, 22.0, 24.3, 27.3, 14.6, 3],
        [160.0, 20.5, 22.5, 25.3, 27.8, 15.1, 3],
        [140.0, 21.0, 22.5, 25.0, 26.2, 13.3, 3],
        [160.0, 21.1, 22.5, 25.0, 25.6, 15.2, 3],
        [169.0, 22.0, 24.0, 27.2, 27.7, 14.1, 3],
        [161.0, 22.0, 23.4, 26.7, 25.9, 13.6, 3],
        [200.0, 22.1, 23.5, 26.8, 27.6, 15.4, 3],
        [180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 3],
        [290.0, 24.0, 26.0, 29.2, 30.4, 15.4, 3],
        [272.0, 25.0, 27.0, 30.6, 28.0, 15.6, 3],
        [390.0, 29.5, 31.7, 35.0, 27.1, 15.3, 3],
        [55.0, 13.5, 14.7, 16.5, 41.5, 14.1, 4],
        [60.0, 14.3, 15.5, 17.4, 37.8, 13.3, 4],
        [90.0, 16.3, 17.7, 19.8, 37.4, 13.5, 4],
        [120.0, 17.5, 19.0, 21.3, 39.4, 13.7, 4],
        [150.0, 18.4, 20.0, 22.4, 39.7, 14.7, 4],
        [140.0, 19.0, 20.7, 23.2, 36.8, 14.2, 4],
        [170.0, 19.0, 20.7, 23.2, 40.5, 14.7, 4],
        [145.0, 19.8, 21.5, 24.1, 40.4, 13.1, 4],
        [200.0, 21.2, 23.0, 25.8, 40.1, 14.2, 4],
        [273.0, 23.0, 25.0, 28.0, 39.6, 14.8, 4],
        [300.0, 24.0, 26.0, 29.0, 39.2, 14.6, 4],
        [6.7, 9.3, 9.8, 10.8, 16.1, 9.7, 5],
        [7.5, 10.0, 10.5, 11.6, 17.0, 10.0, 5],
        [7.0, 10.1, 10.6, 11.6, 14.9, 9.9, 5],
        [9.7, 10.4, 11.0, 12.0, 18.3, 11.5, 5],
        [9.8, 10.7, 11.2, 12.4, 16.8, 10.3, 5],
        [8.7, 10.8, 11.3, 12.6, 15.7, 10.2, 5],
        [10.0, 11.3, 11.8, 13.1, 16.9, 9.8, 5],
        [9.9, 11.3, 11.8, 13.1, 16.9, 8.9, 5],
        [9.8, 11.4, 12.0, 13.2, 16.7, 8.7, 5],
        [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 5],
        [13.4, 11.7, 12.4, 13.5, 18.0, 9.4, 5],
        [12.2, 12.1, 13.0, 13.8, 16.5, 9.1, 5],
        [19.7, 13.2, 14.3, 15.2, 18.9, 13.6, 5],
        [19.9, 13.8, 15.0, 16.2, 18.1, 11.6, 5],
        [200.0, 30.0, 32.3, 34.8, 16.0, 9.7, 6],
        [300.0, 31.7, 34.0, 37.8, 15.1, 11.0, 6],
        [300.0, 32.7, 35.0, 38.8, 15.3, 11.3, 6],
        [300.0, 34.8, 37.3, 39.8, 15.8, 10.1, 6],
        [430.0, 35.5, 38.0, 40.5, 18.0, 11.3, 6],
        [345.0, 36.0, 38.5, 41.0, 15.6, 9.7, 6],
        [456.0, 40.0, 42.5, 45.5, 16.0, 9.5, 6],
        [510.0, 40.0, 42.5, 45.5, 15.0, 9.8, 6],
        [540.0, 40.1, 43.0, 45.8, 17.0, 11.2, 6],
        [500.0, 42.0, 45.0, 48.0, 14.5, 10.2, 6],
        [567.0, 43.2, 46.0, 48.7, 16.0, 10.0, 6],
        [770.0, 44.8, 48.0, 51.2, 15.0, 10.5, 6],
        [950.0, 48.3, 51.7, 55.1, 16.2, 11.2, 6],
        [1250.0, 52.0, 56.0, 59.7, 17.9, 11.7, 6],
        [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 6],
        [1550.0, 56.0, 60.0, 64.0, 15.0, 9.6, 6],
        [1650.0, 59.0, 63.4, 68.0, 15.9, 11.0, 6],
        [5.9, 7.5, 8.4, 8.8, 24.0, 16.0, 7],
        [32.0, 12.5, 13.7, 14.7, 24.0, 13.6, 7],
        [40.0, 13.8, 15.0, 16.0, 23.9, 15.2, 7],
        [51.5, 15.0, 16.2, 17.2, 26.7, 15.3, 7],
        [70.0, 15.7, 17.4, 18.5, 24.8, 15.9, 7],
        [100.0, 16.2, 18.0, 19.2, 27.2, 17.3, 7],
        [78.0, 16.8, 18.7, 19.4, 26.8, 16.1, 7],
        [80.0, 17.2, 19.0, 20.2, 27.9, 15.1, 7],
        [85.0, 17.8, 19.6, 20.8, 24.7, 14.6, 7],
        [85.0, 18.2, 20.0, 21.0, 24.2, 13.2, 7],
        [110.0, 19.0, 21.0, 22.5, 25.3, 15.8, 7],
        [115.0, 19.0, 21.0, 22.5, 26.3, 14.7, 7],
        [125.0, 19.0, 21.0, 22.5, 25.3, 16.3, 7],
        [130.0, 19.3, 21.3, 22.8, 28.0, 15.5, 7],
        [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 7],
        [120.0, 20.0, 22.0, 23.5, 24.0, 15.0, 7],
        [130.0, 20.0, 22.0, 23.5, 26.0, 15.0, 7],
        [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 7],
        [110.0, 20.0, 22.0, 23.5, 23.5, 17.0, 7],
        [130.0, 20.5, 22.5, 24.0, 24.4, 15.1, 7],
        [150.0, 20.5, 22.5, 24.0, 28.3, 15.1, 7],
        [145.0, 20.7, 22.7, 24.2, 24.6, 15.0, 7],
        [150.0, 21.0, 23.0, 24.5, 21.3, 14.8, 7],
        [170.0, 21.5, 23.5, 25.0, 25.1, 14.9, 7],
        [225.0, 22.0, 24.0, 25.5, 28.6, 14.6, 7],
        [145.0, 22.0, 24.0, 25.5, 25.0, 15.0, 7],
        [188.0, 22.6, 24.6, 26.2, 25.7, 15.9, 7],
        [180.0, 23.0, 25.0, 26.5, 24.3, 13.9, 7],
        [197.0, 23.5, 25.6, 27.0, 24.3, 15.7, 7],
        [218.0, 25.0, 26.5, 28.0, 25.6, 14.8, 7],
        [300.0, 25.2, 27.3, 28.7, 29.0, 17.9, 7],
        [260.0, 25.4, 27.5, 28.9, 24.8, 15.0, 7],
        [265.0, 25.4, 27.5, 28.9, 24.4, 15.0, 7],
        [250.0, 25.4, 27.5, 28.9, 25.2, 15.8, 7],
        [250.0, 25.9, 28.0, 29.4, 26.6, 14.3, 7],
        [300.0, 26.9, 28.7, 30.1, 25.2, 15.4, 7],
        [320.0, 27.8, 30.0, 31.6, 24.1, 15.1, 7],
        [514.0, 30.5, 32.8, 34.0, 29.5, 17.7, 7],
        [556.0, 32.0, 34.5, 36.5, 28.1, 17.5, 7],
        [840.0, 32.5, 35.0, 37.3, 30.8, 20.9, 7],
        [685.0, 34.0, 36.5, 39.0, 27.9, 17.6, 7],
        [700.0, 34.0, 36.0, 38.3, 27.7, 17.6, 7],
        [700.0, 34.5, 37.0, 39.4, 27.5, 15.9, 7],
        [690.0, 34.6, 37.0, 39.3, 26.9, 16.2, 7],
        [900.0, 36.5, 39.0, 41.4, 26.9, 18.1, 7],
        [650.0, 36.5, 39.0, 41.4, 26.9, 14.5, 7],
        [820.0, 36.6, 39.0, 41.3, 30.1, 17.8, 7],
        [850.0, 36.9, 40.0, 42.3, 28.2, 16.8, 7],
        [900.0, 37.0, 40.0, 42.5, 27.6, 17.0, 7],
        [1015.0, 37.0, 40.0, 42.4, 29.2, 17.6, 7],
        [820.0, 37.1, 40.0, 42.5, 26.2, 15.6, 7],
        [1100.0, 39.0, 42.0, 44.6, 28.7, 15.4, 7],
        [1000.0, 39.8, 43.0, 45.2, 26.4, 16.1, 7],
        [1100.0, 40.1, 43.0, 45.5, 27.5, 16.3, 7],
        [1000.0, 40.2, 43.5, 46.0, 27.4, 17.7, 7],
        [1000.0, 41.1, 44.0, 46.6, 26.8, 16.3, 7]]


class decisionnode(object):
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb


def sporedi_broj(value1, value2):
    return value1 >= value2


def sporedi_string(value1, value2):
    return value1 == value2


# In[43]:


def get_compare_func(value):
    if isinstance(value, int) or isinstance(value, float):
        comparer = sporedi_broj
    else:
        comparer = sporedi_string
    return comparer

def compare_values(v1, v2):
    sporedi = get_compare_func(v1)
    return sporedi(v1, v2)

def divideset(rows, column, value):
    sporedi = get_compare_func(value)
#     print(split_function)
    # Divide the rows into two sets and return them
    set_false = []
    set_true = []
    for row in rows:
        uslov=sporedi(row[column], value)
#         print(column, value, row[column], uslov, row)
        if uslov:
            set_true.append(row)
        else:
            set_false.append(row)
#     print(len(set_true), len(set_false))
#     set_true = [row for row in rows if
#             split_function(row, column, value)]  # za sekoj row od rows za koj split_function vrakja true
#     set_false = [row for row in rows if
#             not split_function(row, column, value)]  # za sekoj row od rows za koj split_function vrakja false
    return (set_true, set_false)

def uniquecounts(rows):
    d={}
    for r in rows:
#         print(r[-1])
        d.setdefault(r[-1], 0)
        d[r[-1]]+=1
    return d

from math import log
log2 = lambda x: log(x)/log(2)

def entropy(rows):
    results = uniquecounts(rows)
    # Now calculate the entropy
    ent = 0.0
    n = len(rows)
    for label, cnt in results.items():
#         print(r)
        p = float(cnt) / n
#         print(label, cnt, p)
        ent -= p * log2(p)
    return ent

def info_gain(current_score, sets, scoref=entropy):
    m = sum([len(s) for s in sets])
    gain = current_score
    for s in sets:
        n=len(s)
        p=1.*n/m
        gain -= p*scoref(s)
    return gain


def buildtree(rows, scoref=entropy):
    if len(rows) == 0:
        return decisionnode()
    current_score = scoref(rows)

    # Set up some variables to track the best criteria
    best_gain = 0.0
    best_column = -1
    best_value = None
    best_subsetf = None
    best_subsett = None

    column_count = len(rows[0]) - 1
    for col in range(column_count):
        # Generate the list of different values in
        # this column
        #         column_values = set()
        #         for row in rows:
        #             column_values.add(row[col])
        #         print(column_values)
        column_values = set([row[col] for row in rows])
        #         print('Zemame vo predvid podelba po:', col, len(column_values), column_values)
        #         continue
        # Now try dividing the rows up for each value
        # in this column
        for value in column_values:
            sets = divideset(rows, col, value)

            # Information gain
            #             p = float(len(set1)) / len(rows)
            #             gain = current_score - p * scoref(set1) - (1 - p) * scoref(set2)
            gain = info_gain(current_score, sets, scoref)
            if gain > best_gain and len(sets) > 0 and len(sets[0]) > 0 and len(sets[1]) > 0:
                best_gain = gain
                best_column = col
                best_value = value
                best_subsett = sets[0]
                best_subsetf = sets[1]
                # best_criteria = (col, value)
                # best_sets = (set1, set2)
    #             print('Dividing dataset', col, value, gain, sets)
    # pronajden e korenot
    #     return
    # Create the subbranches
    if best_gain > 0:
        #         print(best_subsett)
        #         print(best_subsetf)
        #print(best_column, best_value, best_gain)
        #print('Starting true subbranch')
        trueBranch = buildtree(best_subsett, scoref)
        #print()
        #print('Starting false subbranch')
        falseBranch = buildtree(best_subsetf, scoref)
        #print()
        return decisionnode(col=best_column, value=best_value,
                            tb=trueBranch, fb=falseBranch)

    else:
        #print('Terminalen jazol')
        #print()
        return decisionnode(results=uniquecounts(rows))

def printtree(tree, indent=''):
    # Is this a leaf node?
    if tree.results != None:
        print(indent + str(sorted(tree.results.items())))
    else:
        # Print the criteria
        print(indent + str(tree.col) + ':' + str(tree.value) + '? ')
        # Print the branches
        print(indent + 'T->')
        printtree(tree.tb, indent + '  ')
        print(indent + 'F->')
        printtree(tree.fb, indent + '  ')

def classify(observation, tree):
    if tree.results != None:
#         return tree.results
        if len(tree.results)==1:
            return list(tree.results.keys())[0]
        else:
            inv = sorted([(cnt, label) for label, cnt in tree.results.items()], reverse=True)
            label = inv[0][1]
            cnt = inv[0][0]
            total_count = sum(tree.results.values())
            return label, cnt/total_count
#         return tree.results
    else:
        vrednost = observation[tree.col]
        if compare_values(vrednost, tree.value):
           branch = tree.tb
        else:
           branch = tree.fb
        return classify(observation, branch)


if __name__ == "__main__":

    t1, f1 = divideset(data, -1, 1)
    t2, f2 = divideset(data, -1, 2)
    t3, f3 = divideset(data, -1, 3)
    t4, f4 = divideset(data, -1, 4)
    t5, f5 = divideset(data, -1, 5)
    t6, f6 = divideset(data, -1, 6)
    t7, f7 = divideset(data, -1, 7)

    t = []
    t.extend(t1[0:5])
    t.extend(t2[0:5])
    t.extend(t3[0:5])
    t.extend(t4[0:5])
    t.extend(t5[0:5])
    t.extend(t6[0:5])
    t.extend(t7[0:5])

    d = buildtree(t)
    index = int(input())
    testCase = data[index]
    c = classify(testCase, d)
    print(c)
