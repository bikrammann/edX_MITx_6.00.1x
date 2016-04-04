def getSublists(L, n):
    assert (0 < n <= len(L))
    result=[]
    for i in range(len(L)-n+1):
        T =L[i:i+n]
        result.append(T)
    return result