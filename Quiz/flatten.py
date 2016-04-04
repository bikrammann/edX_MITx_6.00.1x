def flatten(aList):
    """
    Flatten a list containing other lists, strings, or ints.
    Example: [[1,'a',['cat'],2],[[[3]],'dog'],4,5] => [1,'a','cat',2,3,'dog',4,5]
    """

    newList = []

    for elt in aList:
        if type(elt) == type([]):
            inner = flatten(elt)
            newList += inner
        else:
            newList.append(elt)
    return newList