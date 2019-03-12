"""
Дрва за одлучување (80 поени) Problem 1 (0 / 0)
Да се промени функцијата за предвидување, така што при изминувањето ќе печати информации за:

со која колона и вредност се споредува
за која е тековната вредност на тест примерокот за бараната колона
која е следната гранка што ќе се изминува низ дрвото (True branch или False branch)
преостанатиот дел од дрвото што треба да се измине
празна линија
Потоа да се испечати истренираното дрво, да се вчита непознат тренинг примерок од стандардниот влез и
истиот да се класифицира со новата функција за предвидување.
# trainingData=[line.split('\t') for line in file('decision_tree_example.txt')]


"""

trainingData = [['slashdot', 'USA', 'yes', 18, 'None'],
                ['google', 'France', 'yes', 23, 'Premium'],
                ['google', 'France', 'yes', 23, 'Basic'],
                ['google', 'France', 'yes', 23, 'Basic'],
                ['digg', 'USA', 'yes', 24, 'Basic'],
                ['kiwitobes', 'France', 'yes', 23, 'Basic'],
                ['google', 'UK', 'no', 21, 'Premium'],
                ['(direct)', 'New Zealand', 'no', 12, 'None'],
                ['(direct)', 'UK', 'no', 21, 'Basic'],
                ['google', 'USA', 'no', 24, 'Premium'],
                ['slashdot', 'France', 'yes', 19, 'None'],
                ['digg', 'USA', 'no', 18, 'None'],
                ['google', 'UK', 'no', 18, 'None'],
                ['kiwitobes', 'UK', 'no', 19, 'None'],
                ['digg', 'New Zealand', 'yes', 12, 'Basic'],
                ['slashdot', 'UK', 'no', 21, 'None'],
                ['google', 'UK', 'yes', 18, 'Basic'],
                ['kiwitobes', 'France', 'yes', 19, 'Basic']]


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
        lista = []
        maxi = 0

        for i in tree.results.keys():
            if tree.results[i] > maxi:
                maxi = tree.results[i]

        for i in tree.results.keys():
            if tree.results[i] == maxi:
                lista.append((i))

        lista.sort()
        return lista[0]

    else:
        vrednost = observation[tree.col]

        print("Se sporeduva so kolonata: ",tree.col)
        print("Se sporeduva so vrednosta: ",tree.value)
        print("Tekovnata vrednost na primerokot: ",vrednost)

        if compare_values(vrednost, tree.value):
           print("Slednata granka koja ke se izminuva e True branch")
           branch = tree.tb
        else:

           print("Slednata granka koja ke se izminuva e False branch")
           branch = tree.fb
        return classify(observation, branch)


if __name__=="__main__":

    #testCase = input()
    testCase = ['google', 'France', 'yes', 23, 'Basic']

    t = buildtree(trainingData)
    c = classify(testCase, t)
    print(c)


