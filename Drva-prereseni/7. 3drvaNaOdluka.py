"""
Да се промени алгоритмот за дрво на одлука така што ќе се изградат 3 дрва на одлука.
Првото дрво ќе ги содржи првите десет членови од податочното множество од секоја од трите класи,
второто вторите десет од секоја класа, а третото третите десет од секоја класа на податочното множество.
Да се промени начинот на одлука така што на излез ќе се печати класата за која изгласале мнозинството од дрвата.
Доколку сите 3 дрва одлучат различно да се испечати unknown. Доколку некое од дрвата има само една класа тогаш се
предвидува истата, но ако има повеќе од една треба да се избере таа со најголем број на инстанци. Ако во листот има
неколку класи со ист број на инстанци да се предвиде првата класа по азбучен ред.

"""
trainingData=[[5.1,3.5,1.4,0.2,'I. setosa'],
[4.9,3.0,1.4,0.2,'I. setosa'],
[4.7,3.2,1.3,0.2,'I. setosa'],
[4.6,3.1,1.5,0.2,'I. setosa'],
[5.0,3.6,1.4,0.2,'I. setosa'],
[5.4,3.9,1.7,0.4,'I. setosa'],
[4.6,3.4,1.4,0.3,'I. setosa'],
[5.0,3.4,1.5,0.2,'I. setosa'],
[4.4,2.9,1.4,0.2,'I. setosa'],
[4.9,3.1,1.5,0.1,'I. setosa'],
[5.4,3.7,1.5,0.2,'I. setosa'],
[4.8,3.4,1.6,0.2,'I. setosa'],
[4.8,3.0,1.4,0.1,'I. setosa'],
[4.3,3.0,1.1,0.1,'I. setosa'],
[5.8,4.0,1.2,0.2,'I. setosa'],
[5.7,4.4,1.5,0.4,'I. setosa'],
[5.4,3.9,1.3,0.4,'I. setosa'],
[5.1,3.5,1.4,0.3,'I. setosa'],
[5.7,3.8,1.7,0.3,'I. setosa'],
[5.1,3.8,1.5,0.3,'I. setosa'],
[5.4,3.4,1.7,0.2,'I. setosa'],
[5.1,3.7,1.5,0.4,'I. setosa'],
[4.6,3.6,1.0,0.2,'I. setosa'],
[5.1,3.3,1.7,0.5,'I. setosa'],
[4.8,3.4,1.9,0.2,'I. setosa'],
[5.0,3.0,1.6,0.2,'I. setosa'],
[5.0,3.4,1.6,0.4,'I. setosa'],
[5.2,3.5,1.5,0.2,'I. setosa'],
[5.2,3.4,1.4,0.2,'I. setosa'],
[4.7,3.2,1.6,0.2,'I. setosa'],
[4.8,3.1,1.6,0.2,'I. setosa'],
[5.4,3.4,1.5,0.4,'I. setosa'],
[5.2,4.1,1.5,0.1,'I. setosa'],
[5.5,4.2,1.4,0.2,'I. setosa'],
[4.9,3.1,1.5,0.2,'I. setosa'],
[5.0,3.2,1.2,0.2,'I. setosa'],
[5.5,3.5,1.3,0.2,'I. setosa'],
[4.9,3.6,1.4,0.1,'I. setosa'],
[4.4,3.0,1.3,0.2,'I. setosa'],
[5.1,3.4,1.5,0.2,'I. setosa'],
[5.0,3.5,1.3,0.3,'I. setosa'],
[4.5,2.3,1.3,0.3,'I. setosa'],
[4.4,3.2,1.3,0.2,'I. setosa'],
[5.0,3.5,1.6,0.6,'I. setosa'],
[5.1,3.8,1.9,0.4,'I. setosa'],
[4.8,3.0,1.4,0.3,'I. setosa'],
[5.1,3.8,1.6,0.2,'I. setosa'],
[5.5,2.3,4.0,1.3,'I. versicolor'],
[6.5,2.8,4.6,1.5,'I. versicolor'],
[5.7,2.8,4.5,1.3,'I. versicolor'],
[6.3,3.3,4.7,1.6,'I. versicolor'],
[4.9,2.4,3.3,1.0,'I. versicolor'],
[6.6,2.9,4.6,1.3,'I. versicolor'],
[5.2,2.7,3.9,1.4,'I. versicolor'],
[5.0,2.0,3.5,1.0,'I. versicolor'],
[5.9,3.0,4.2,1.5,'I. versicolor'],
[6.0,2.2,4.0,1.0,'I. versicolor'],
[6.1,2.9,4.7,1.4,'I. versicolor'],
[5.6,2.9,3.6,1.3,'I. versicolor'],
[6.7,3.1,4.4,1.4,'I. versicolor'],
[5.6,3.0,4.5,1.5,'I. versicolor'],
[5.8,2.7,4.1,1.0,'I. versicolor'],
[6.2,2.2,4.5,1.5,'I. versicolor'],
[5.6,2.5,3.9,1.1,'I. versicolor'],
[5.9,3.2,4.8,1.8,'I. versicolor'],
[6.1,2.8,4.0,1.3,'I. versicolor'],
[6.3,2.5,4.9,1.5,'I. versicolor'],
[6.1,2.8,4.7,1.2,'I. versicolor'],
[6.4,2.9,4.3,1.3,'I. versicolor'],
[6.6,3.0,4.4,1.4,'I. versicolor'],
[6.8,2.8,4.8,1.4,'I. versicolor'],
[6.7,3.0,5.0,1.7,'I. versicolor'],
[6.0,2.9,4.5,1.5,'I. versicolor'],
[5.7,2.6,3.5,1.0,'I. versicolor'],
[5.5,2.4,3.8,1.1,'I. versicolor'],
[5.5,2.4,3.7,1.0,'I. versicolor'],
[5.8,2.7,3.9,1.2,'I. versicolor'],
[6.0,2.7,5.1,1.6,'I. versicolor'],
[5.4,3.0,4.5,1.5,'I. versicolor'],
[6.0,3.4,4.5,1.6,'I. versicolor'],
[6.7,3.1,4.7,1.5,'I. versicolor'],
[6.3,2.3,4.4,1.3,'I. versicolor'],
[5.6,3.0,4.1,1.3,'I. versicolor'],
[5.5,2.5,4.0,1.3,'I. versicolor'],
[5.5,2.6,4.4,1.2,'I. versicolor'],
[6.1,3.0,4.6,1.4,'I. versicolor'],
[5.8,2.6,4.0,1.2,'I. versicolor'],
[5.0,2.3,3.3,1.0,'I. versicolor'],
[5.6,2.7,4.2,1.3,'I. versicolor'],
[5.7,3.0,4.2,1.2,'I. versicolor'],
[5.7,2.9,4.2,1.3,'I. versicolor'],
[6.2,2.9,4.3,1.3,'I. versicolor'],
[5.1,2.5,3.0,1.1,'I. versicolor'],
[5.7,2.8,4.1,1.3,'I. versicolor'],
[6.3,2.9,5.6,1.8,'I. virginica'],
[6.5,3.0,5.8,2.2,'I. virginica'],
[7.6,3.0,6.6,2.1,'I. virginica'],
[4.9,2.5,4.5,1.7,'I. virginica'],
[7.3,2.9,6.3,1.8,'I. virginica'],
[6.7,2.5,5.8,1.8,'I. virginica'],
[7.2,3.6,6.1,2.5,'I. virginica'],
[6.5,3.2,5.1,2.0,'I. virginica'],
[6.4,2.7,5.3,1.9,'I. virginica'],
[6.8,3.0,5.5,2.1,'I. virginica'],
[5.7,2.5,5.0,2.0,'I. virginica'],
[5.8,2.8,5.1,2.4,'I. virginica'],
[6.4,3.2,5.3,2.3,'I. virginica'],
[6.5,3.0,5.5,1.8,'I. virginica'],
[7.7,3.8,6.7,2.2,'I. virginica'],
[7.7,2.6,6.9,2.3,'I. virginica'],
[6.0,2.2,5.0,1.5,'I. virginica'],
[6.9,3.2,5.7,2.3,'I. virginica'],
[5.6,2.8,4.9,2.0,'I. virginica'],
[7.7,2.8,6.7,2.0,'I. virginica'],
[6.3,2.7,4.9,1.8,'I. virginica'],
[6.7,3.3,5.7,2.1,'I. virginica'],
[7.2,3.2,6.0,1.8,'I. virginica'],
[6.2,2.8,4.8,1.8,'I. virginica'],
[6.1,3.0,4.9,1.8,'I. virginica'],
[6.4,2.8,5.6,2.1,'I. virginica'],
[7.2,3.0,5.8,1.6,'I. virginica'],
[7.4,2.8,6.1,1.9,'I. virginica'],
[7.9,3.8,6.4,2.0,'I. virginica'],
[6.4,2.8,5.6,2.2,'I. virginica'],
[6.3,2.8,5.1,1.5,'I. virginica'],
[6.1,2.6,5.6,1.4,'I. virginica'],
[7.7,3.0,6.1,2.3,'I. virginica'],
[6.3,3.4,5.6,2.4,'I. virginica'],
[6.4,3.1,5.5,1.8,'I. virginica'],
[6.0,3.0,4.8,1.8,'I. virginica'],
[6.9,3.1,5.4,2.1,'I. virginica'],
[6.7,3.1,5.6,2.4,'I. virginica'],
[6.9,3.1,5.1,2.3,'I. virginica'],
[5.8,2.7,5.1,1.9,'I. virginica'],
[6.8,3.2,5.9,2.3,'I. virginica'],
[6.7,3.3,5.7,2.5,'I. virginica'],
[6.7,3.0,5.2,2.3,'I. virginica'],
[6.3,2.5,5.0,1.9,'I. virginica'],
[6.5,3.0,5.2,2.0,'I. virginica'],
[6.2,3.4,5.4,2.3,'I. virginica'],
[5.9,3.0,5.1,1.8,'I. virginica']]

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
            return list(tree.results.keys())[0], 1.0
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


if __name__=="__main__":

    t11, f11 = divideset(trainingData, -1, 'I. setosa')
    t12, f12 = divideset(trainingData, -1, 'I. virginica')
    t13, f13 = divideset(trainingData, -1, 'I. virginica')

    t1 = []
    t1.extend(t11[0:10])
    t1.extend(t12[0:10])
    t1.extend(t13[0:10])

    t21, f21 = divideset(trainingData, -1, 'I. setosa')
    t22, f22 = divideset(trainingData, -1, 'I. virginica')
    t23, f23 = divideset(trainingData, -1, 'I. virginica')

    t2 = []
    t2.extend(t21[10:20])
    t2.extend(t22[10:20])
    t2.extend(t23[10:20])

    t31, f31 = divideset(trainingData, -1, 'I. setosa')
    t32, f32 = divideset(trainingData, -1, 'I. virginica')
    t33, f33 = divideset(trainingData, -1, 'I. virginica')

    t3 = []
    t3.extend(t31[20:30])
    t3.extend(t32[20:30])
    t3.extend(t33[20:30])

    d1 = buildtree(t1)
    d2 = buildtree(t2)
    d3 = buildtree(t3)

    testCase = [6.5,3.2,5.1,2.0,'unknown']
    c1 = classify(testCase, d1)
    c2 = classify(testCase, d2)
    c3 = classify(testCase, d3)

    print(c1, c2, c3)

    if c1==c2 and c2==c3 and c1==c3:
        print(c1)
    else:
        print("unknown")