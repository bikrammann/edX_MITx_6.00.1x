def getSublists(L, n):
    assert (0 < n <= len(L))
    result=[]
    for i in range(len(L)-n+1):
        T =L[i:i+n]
        result.append(T)
    return result

def longestRun(L):

    for x in range(len(L),0,-1):
        subL=getSublists(L, x)
        for y in range(len(subL)):
            result=True
            list=subL[y]
            for z in range(len(list)-1):
                if list[z]> list[z+1]:
                    result=False
            if result==True:
                output=x
                return output