def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """

    l1 = L[:]

    for elt in l1:
        if not f(elt):
            L.remove(elt)
    return len(L)

run_satisfiesF(L, satisfiesF)