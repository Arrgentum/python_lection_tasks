def check(): 
    a = input()
    b = [0,0,0,0,len(a)]
    #0 - heigth, 1 - width, 2 - quantiry "*", 3 - count str, 4 - length str
    while bool(a):
        b[3] += 1
        c = -1
        i = 0
        while i < len(a):
            if a[i] == "#":
                if c < 0:
                    b[0] += 1
                    c = i
                elif b[1] == 0:
                    b[1] = i - c + 1
            elif a[i] == "*" and c >= 0:
                b[2] += 1
            i += 1
        a = input()

    return b

def makestr(b):
    a = ["#", "#", "*", "."]
    i = 1
    while i < b[4]:
        if i < b[0]:
            a[0] += "#"
        else:
            a[0] += "."
        a[1] += "."
        a[2] += "*"
        a[3] += "."
        i += 1
    return a

def output(a , b):
    i = 0
    c = 1
    if b[2] % b[4] == 0:
        c = 0
    d =  b[2] / b[4] + c
    while i < b[3]:
        if b[3] - i < d:
            print(a[2])
        elif (b[3] - i == b[1]) or (d == 0 and i + 1 == b[3]) :
            print(a[0])
        elif b[3] - i < b[1] and b[3] - i > d:
            print(a[1])
        else:
            print(a[3])
        i += 1
    return


info = check()
# print(info)
strings = makestr(info)
output(strings, info)

