def merge_dicts(x,y):
    """
    Merges two dictionaries together and returns new dict
    """
    z = x.copy()
    z.update(y)
    return z


def dict_interdiff(d1, d2):
    """
    d1, d2 are dicts whose keys and values are integers
    Returns a tuple of two dictionaries: A dictionary of the intersect of d1 and d2
    and a dictionary of the difference of d1 and d2

    Assumes function f is defined, that takes in two integers and performs
    an unknown operation on them and returns a value
    """

    intersect = set(d1.keys()) & set(d2.keys())
    newdict = merge_dicts(d1,d2)

    c1 = {}
    c2 = {}

    for n in intersect:
       c1[n] =  f(d1[n],d2[n])

    for n in newdict.keys():
        if not n in intersect:
            c2[n]= newdict[n]

    return c1, c2