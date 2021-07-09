import random
import math
from math import sqrt

def randsquare(a, b):
    def seach(a, b):
        m = (((max(a[0], b[0]) - min(a[0], b[0]))**2 + (max(a[1], b[1]) - min(a[1], b[1]))**2 )**(1/2) ) / 2
        xc = a[0] + (b[0] - a[0])/2
        yc = a[1] + (b[1] - a[1])/2
        if a[0] == b[0]:
            c = (a[0] - m, yc)
            d = (a[0] + m, yc)
        elif a[1] == b[1]:
            c = (xc , a[1] - m)
            d = (xc, a[1] + m)
        else:
            u = math.atan((b[1] - yc)/(b[0] - xc))
            c= (xc + m*math.cos(u + math.pi/2) , yc + m*math.sin(u + math.pi/2))
            d= (xc + m*math.cos(u - math.pi/2) , yc + m*math.sin(u - math.pi/2))
        return c, d

    def f(i, j, random):
        l = (random - i[0]) / (j[0] - i[0])
        return (j[1] - i[1]) * l + i[1]

    def fun(s,v,n,m,rand1):
        #print(s,v,n,m)
        if rand1 < n[0] and rand1 > s[0]:
            u1 = f(s,n, rand1)
        else:
            u1 = f(n, v, rand1)
        if rand1 < m[0] and rand1 > s[0]:
            u2 = f(s, m, rand1)
        else:
            u2 = f(m, v, rand1)
        #print(rand1 , u1, u2)
        return u1, u2

    c, d = seach(a, b)
    x = max(max(a[0], b[0]) -min(a[0], b[0]), max(c[0], d[0]) -min(c[0], d[0]))
    xmin = min(a[0], b[0], c[0], d[0])
    xrandom = random.uniform(xmin, xmin + x)
    if xmin == a[0]:
        l1, l2 = fun(a,b,c,d,xrandom)
        yrandom = random.uniform(l1, l2)
    elif xmin == b[0]:
        l1, l2 = fun(b,a,c,d,xrandom)
        yrandom = random.uniform(l1, l2)
    elif xmin == c[0]:
        l1, l2 = fun(c,d,a,b,xrandom)
        yrandom = random.uniform(l1, l2)
    else:
        l1, l2 = fun(d,c,a,b,xrandom)
        yrandom = random.uniform(l1, l2)
    return xrandom, yrandom
