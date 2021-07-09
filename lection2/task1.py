import math

a, b, c = eval(input())
x1 = 0
x2 = 0
d = 0

if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        x2 = -c/b
        if x2 > 0:
             print(x1, x2)
        else:
             print(x2, x1)
else:
    if b == 0:
        x1 = math.sqrt(c/a)
        print(x1, x1)
    else:
        d = b*b - 4*a*c
        if d >= 0:
            d = math.sqrt(d)
            x1 = (-b-d)/(2*a)
            x2 = (-b+d)/(2*a)
            if x1 > x2:
                print(x2, x1)
            elif x1 == x2:
                print(x2)
            else:
                print(x1, x2)
        else:
            print(0)
