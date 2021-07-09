b = eval(input())
a = input()
D = dict()
string = ",*()[]{}-=_.;%$@3^&\|#':?!" + "\""
while bool(a):
    a = a.lower()
    for i in string:
        a = a.replace(i, " ")
    for i in a.split():
        if len(i) >=  b[1]:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
    a = input()
L = dict()
for i in D:
    c = D[i]
    if c in L:
        L[c].append(i)
    else:
        L[c] = [i]
c = len(L)
L = list( [i, L[i]] for i in L)
L = sorted(L)
a = 1
for i in L:
    if a > c - b[0]:
        i[1] = sorted(i[1])
        for j in i[1]:
            h = str(i[0])
            if j.isalpha():
                h = h +":"
                print(h, j)
    a += 1
