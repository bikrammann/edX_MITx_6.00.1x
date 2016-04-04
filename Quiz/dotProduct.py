def dotProduct(listA, listB):
    """
    Assumes listA and listB are of same length and are two lists of integer numbers
    Returns pairwise products of listA and listB
    """
    l1 = listA[:]
    l2 = listB[:]
    total = 0

    for x, y in zip(l1,l2):
        total += x*y

    return total