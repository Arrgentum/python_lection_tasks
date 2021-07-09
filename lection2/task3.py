b = False
min1 = list()
max1 = list()
x = input()
while bool(x):
    x = eval(x)
    if b == False:
        b = True
        max1 = list(x)
        min1 = list(x)
    i = 0
    while i < 3:
        if x[i] > max1[i]:
            max1[i] = x[i]
        elif x[i] < min1[i]:
            min1[i] = x[i]
        i += 1
    x = input()

print((max1[0]-min1[0])*(max1[1]-min1[1])*(max1[2]-min1[2]))
