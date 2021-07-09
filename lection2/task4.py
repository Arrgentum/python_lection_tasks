max_sum = sum1 = elem = int(input())
while elem != 0:
    elem = int(input())
    sum1 += elem
    if sum1 < elem and elem != 0:
        sum1 = elem
    if sum1 > max_sum:
        max_sum = sum1
print(max_sum)

