from decimal import Decimal as dec, getcontext
from decimal import *
from math import factorial

def PiGen():
    getcontext().prec = 10000
    sum1 = dec()
    first = dec(10005).sqrt() * 426800
    for m in range(1000):
        add = Decimal((factorial(6*m) * (545140134*m + 13591409)) / ( (factorial(3*m)) * (factorial(m) ** 3) * ((-262537412640768000)**m)))
        sum1 += add / first
        yield 1/sum1
