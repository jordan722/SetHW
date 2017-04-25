def Union(set1, set2):
    return set1 + [x for x in set2 if x not in set1]

def Intersect(set1, set2):
    return [x for x in set1 if x in set2]

def SetDiff(set1, set2):
    return [x for x in set1 if x not in set2]

def SymmDiff(set1, set2):
    setA = SetDiff(set1, set2)
    setB = SetDiff(set2, set1)
    return setA + setB

def CarProduct(set1, set2):
    return [(x,y) for x in set1 for y in set2]
