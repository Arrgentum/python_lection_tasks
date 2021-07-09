def step(N,K):
    if N == 1:
        return (K-1, 0, 0)
    elif N > 1:
        b = step(N-1,K)
        c = (K-1)*(K**(N-1)) 
        return (c - b[0] - b[1]*K -b[2] ,b[2] + b[1]*K, b[0])
    

def No_2Zero(N,K):
    a = step(N, K)
    return a[0]+a[2]
