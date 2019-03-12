"""
Да се промени класата за дрво на одлука да чува и информација на кое ниво во дрвото се наоѓа јазолот.
Потоа да се променат и функциите за градење и печатење на дрвото така што за секој јазол ќе се печати и нивото.
Коренот е на нулто ниво. На излез со функцијата printTree треба да се испечати даденото тренинг множество.
Прочитана инстанца од стандарден влез да се додаде на тренинг множеството и потоа да се истренира и испечати истото.
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

class decisionnode:
    def __init__(self, col=-1, value=None, results=None, tb=None, fb=None, l=-1):
        self.col = col
        self.value = value
        self.results = results
        self.tb = tb
        self.fb = fb
        self.l = l

def sporedi_broj(row, column, value):
    return row[column] >= value


def sporedi_string(row, column, value):
    return row[column] == value


def divideset(rows, column, value):
    split_function = None
#     print(split_function)
    if isinstance(value, int) or isinstance(value, float):
        split_function = sporedi_broj
    else:
        split_function = sporedi_string
#     print(split_function)
    # Divide the rows into two sets and return them
    set_false = []
    set_true = []
    for row in rows:
        if split_function(row, column, value):
            set_true.append(row)
        else:
            set_false.append(row)
#     print(len(set_true),len(set_false))
    set1 = [row for row in rows if
            split_function(row, column, value)]  # za sekoj row od rows za koj split_function vrakja true
    set2 = [row for row in rows if
            not split_function(row, column, value)]  # za sekoj row od rows za koj split_function vrakja false
    return (set_true, set_false)



def uniquecounts(rows):
    results = {}
    for row in rows:
        # The result is the last column
        r = row[-1]
        results.setdefault(r, 0)
        results[r] += 1

    return results

def log2(x):
    from math import log
    l2 = log(x) / log(2)
    return l2


# Entropy is the sum of p(x)log(p(x)) across all
# the different possible results
def entropy(rows):
    results = uniquecounts(rows)
    # Now calculate the entropy
    ent = 0.0
    for r in results.keys():
        p = float(results[r]) / len(rows)
        ent = ent - p * log2(p)
    return ent


def buildtree(rows, scoref=entropy, l=-1):
    if len(rows) == 0: return decisionnode()
    current_score = scoref(rows)

    # Set up some variables to track the best criteria
    best_gain = 0.0
    best_column = -1
    best_value = None
    best_subsetf = None
    best_subsett = None
    level = l

    column_count = len(rows[0]) - 1
    for col in range(column_count):
        # Generate the list of different values in
        # this column
        column_values = set()
        for row in rows:
            column_values.add(row[col])
        # Now try dividing the rows up for each value
        # in this column
        for value in column_values:
            (set1, set2) = divideset(rows, col, value)

            # Information gain
            p = float(len(set1)) / len(rows)
            gain = current_score - p * scoref(set1) - (1 - p) * scoref(set2)
            if gain > best_gain and len(set1) > 0 and len(set2) > 0:
                best_gain = gain
                best_column = col
                best_value = value
                best_subsett = set1
                best_subsetf = set2
                # best_criteria = (col, value)
                # best_sets = (set1, set2)

    # Create the subbranches
    if best_gain > 0:
        level = level+1
        trueBranch = buildtree(best_subsett, scoref, level)
        falseBranch = buildtree(best_subsetf, scoref,level)
        return decisionnode(col=best_column, value=best_value,
                            tb=trueBranch, fb=falseBranch, l=level)
    else:
        return decisionnode(results=uniquecounts(rows), l=level)

def printtree(tree, indent=''):
    # Is this a leaf node?
    if tree.results != None:
        print(str(tree.results))
    else:
        # Print the criteria
        print(str(tree.col) + ':' + str(tree.value) + '? ') + 'Level=' + str(tree.l)
        # Print the branches
        print(indent + 'T->'),
        printtree(tree.tb, indent + '  ')
        print(indent + 'F->'),
        printtree(tree.fb, indent + '  ')


def classify(observation, tree):
    if tree.results != None:
        return tree.results
    else:
        vrednost = observation[tree.col]
        branch = None

        if isinstance(vrednost, int) or isinstance(vrednost, float):
            if vrednost >= tree.value:
                branch = tree.tb
            else:
                branch = tree.fb
        else:
            if vrednost == tree.value:
                branch = tree.tb
            else:
                branch = tree.fb

        return classify(observation, branch)


if __name__ == "__main__":
    referrer = input()
    location = input()
    readFAQ = input()
    pagesVisited = input()
    serviceChosen = input()

    # referrer = 'google'
    # location = 'UK'
    # readFAQ = 'no',
    # pagesVisited = 18
    # serviceChosen = 'None'

    tmp = [referrer, location, readFAQ, pagesVisited, serviceChosen]
    trainingData.append(tmp)
    t = buildtree(trainingData)

    printtree(t)
