a = input()
c = input()
b = False
i = 0
alen = len(a)
clen = len(c)
while i < alen and not b:
    if a[i] == c[0]:
        j = i+1
        if clen == 1:
            b = True
            break
        while j < alen and not b:
            if a[j] == c[1]:
                k = 0
                while k < clen:
                    if k*(j-i)+i >=  alen or  c[k] != a[k*(j-i) + i]:
                        break
                    k +=1
                else:
                    b = True
            j += 1
    i += 1
if b:
    print("YES")
else:
    print("NO")
