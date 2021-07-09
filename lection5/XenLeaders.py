def seachmax(l):
    s = [-1,-1,-1,-1]
    #print(l)
    #print(max1)
    for i in l:
        for j in l[i]:
            s = [max(s[0], len(j[0])), max(s[1], len(j[1])), max(s[2], len(j[2])), max(s[3], len(j[3]))] 
    return s

def creatlist(i, l, b, max1, max2):
    if i in l:
        l[i].append(b)
    else:
        l.update({i:[b]})
        if len(l) > 3:
            l.pop(max1[2])
    #print(l)

a = input()
l = dict()
max1 = [-1,-2,-3] #maximums
max2 = [0, 0, 0, 0] #size
while bool(a):
    b = a.split(" ")
    i = 3
    while i < len(b)-1:
        b[2] = b[2] +" "+ b[i]
        i+=1
    b = [b[0], b[1], b[2], b[len(b)-1]]
    d = b[3].split(":")
    if len(d[1]) == 1:
        d[1] = "0" + d[1]
    if len(d[2]) == 1:
        d[2] = "0" + d[2]
    s = int(d[0]+d[1]+d[2])
    if max1[0] < 0 or s <= max1[0]:
        creatlist(s, l, b, max1, max2)
        if max1[0] > s or max1[0] < 0:
            max1[2] , max1[1] , max1[0] = max1[1] , max1[0] , s
    elif max1[1] >= s or max1[1] < 0:
        creatlist(s, l, b, max1, max2)
        if max1[1] > s or max1[1] < 0:
            max1[2] , max1[1] = max1[1] , s
    elif max1[2] >= s or max1[2] < 0:
        creatlist(s, l, b, max1, max2)
        if max1[2] > s or max1[2] < 0:
            max1[2] = s
    #print(max1)
    a = input()

max2 = seachmax(l)
s = sorted(list(i for i in l))
for i in l:
    l[i].sort(key = lambda x: x[1])
for i in s:
    for j in l[i]:
        print("{:<{max2[0]}} {:<{max2[1]}} {:<{max2[2]}} {:<{max2[3]}}".format(*j, max2=[max2[0], max2[1], max2[2], max2[3]]))

