from decimal import *

def makefun():
    def newfun1(x):
        def newfun2(x):
            return eval(a)
        return newfun2(x)
    
    a = input()
    return newfun1

def binpoisk(func, n, b, k):
    getcontext().prec = k
    c = Decimal(str((b[1] + b[0]) / 2))
    if abs(1*Decimal(b[1]) -  1*Decimal(b[0])) < 10**(-n-2) :
        print(f"{c:.{n}f}")
        return
    elif func(b[0]) >= 0 and func(b[1]) <= 0:
        if func(c) > 0:
            b[0] = c
        else:
            b[1] = c
    else:
        if func(c) > 0:
            b[1] = c
        else:
            b[0] = c
    k += 1
    return binpoisk(func, n, b, k)

a = makefun()
print(a(30))
c = binpoisk(a , int(input()) , [Decimal('-1.5') , Decimal('1.5')], 2)
