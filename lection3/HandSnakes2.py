b = list()
c = input()
while bool(c):
    c = set(eval(c))
    s = list(set(j for j in range(len(b)) for i in c if i in b[j]))
    s.sort(reverse=True)
    if len(s) > 0:
        for j in s:
            if j < len(b) and b.count(b[j]):
                c.update(b[j])
                b.pop(j)
    b.append(c)
    c = input()
if len(b) > 1:
    print("NO")
else:
    print("YES")
