dict1 = dict() # name : number
dict2 = dict() # number : card
a = input()
while bool(a):
    b = a.split("/")
    if a.find("/") > 4:
        if b[0] in dict1:
            (dict1[b[0]]).add(int(b[1]))
        else:
            dict1[b[0]] = { int(b[1]) }
    else:
        if int(b[0]) in dict2:
            (dict2[int(b[0])]).add(b[1])
        else:
            dict2[int(b[0])] = { b[1] }
    a = input()

def check(dictionary1, dictionary2, names, cards, counter):
    j = 1
    print(names)
    for name in dictionary1:
        print(name)
        if j > counter:
            break
        j += 1
    else:
        return names, cards
    counter += 1
    L = list(j for i in dictionary1[name] for j in dictionary2[i])
    for j in L:
        if j in cards:
            return names, cards
            break
    else:
        names1, cards1 = names, cards
        names1.add(name)
        for i in dictionary1[name]:
            cards1.update(dictionary2[i])
        names1, cards1 = check(dictionary1, dictionary2, names1, cards1, counter)
        names2, cards2 = check(dictionary1, dictionary2, names, cards, counter)
        if len(cards1) > len(cards2):
            return names1, cards1
        else:
            return names2, cards2

name, card = check(dict1, dict2, set(), set(), 0)
for i in sorted(list(name)):
    print(i)
