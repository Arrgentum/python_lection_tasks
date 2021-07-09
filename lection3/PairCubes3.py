a = int(input())
b = a**(1/3)
c =int( b)
while c > 0.75*b:
    d = round((a-c**3)**(1/3))
    if d**3 + c**3 == a:
        print("YES")
        break
    c -= 1
else:
    print("NO")
















