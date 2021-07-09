import math

a = int(input())
i = a
while i > 2:
    b = math.sqrt(i)
    j = 2
    while j < b:
        if i%j == 0:
            break
        j += 1
    else:
        c = i
        print(c)
        break
    i -= 1
    
