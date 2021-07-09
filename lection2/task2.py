max1 = 0
max2 = 0
a = int(input())
while a != 0:
    if a > max1 or max1==0:
        max2 = max1
        max1 = a
    elif a != max1 and (a > max2 or max2 == 0):
        max2 = a
    a = int(input())
if max2 == 0:
    print("NO")
else:
    print(max2)

