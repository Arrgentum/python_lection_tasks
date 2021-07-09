from itertools import tee, islice
def YinYang(*L):
    M = list()
    N = list()
    for i in L:
        k, n = tee(i,2)
        M.append(k)
        N.append(n)
    for i in N:
        for j in i:
            if not j%2:
                yield j
    for i in M:
        #print(i)
        for j in i:
            #print(j)
            if j%2:
                yield j
