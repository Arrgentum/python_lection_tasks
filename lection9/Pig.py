import re

word = re.compile(r"([a-z']+)|([A-Z'][a-z']*)")
vowels = r"[eaoui]"
firstvow = r"([eaoui])([a-z']*)"
firstvowcons = r"([aouie])([^aouie]*)([aouie])([a-z']*)"
firstcons = r"([^aouie]+)([aouie])([a-z']*)"

def translateword(s):
    flag = False
    if s[0].isupper():
        flag = not flag
    s = s.lower()

    if re.fullmatch(firstvow, s) != None:
        if len(re.findall(vowels, s)) == 1:
            res = re.sub(firstvow, r"\1\2yay", s)
        else:
            res = re.sub(firstvowcons, r"\3\4\1\2ay", s)

    elif re.fullmatch(firstcons, s) != None:
        res = re.sub(firstcons, r"\2\3\1ay", s)

    else:
        return s[0].upper() + s[1::] if flag else s
    if flag:
        return res[0].upper() + res[1::]
    else:
        return res

string = input()
while bool(string):
    res = word.sub(lambda x: translateword(x.group()), string)
    print(res)
    string = input()