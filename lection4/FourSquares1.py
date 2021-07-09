a = int(input())
l = list()
b = int(a**(1/2))
i = int(b/2)
while i <= b:
    j = 0
    while j <= i and i*i + j*j <= a:
        k = 0
        while k <= j and i*i + j*j + k*k <= a:
            c = j*j + i*i + k*k
            f = int((a-c)**(1/2))
            if f*f + c == a and f <= k:
                print(i,j,k,f)
            k += 1
        j += 1
    i += 1
