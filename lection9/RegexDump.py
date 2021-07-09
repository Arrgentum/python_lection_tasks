from re import *

string1 = compile(input())
string = input()
while string:
    elem = string1.search(string)
    if elem:
        print(elem.start(), ": ", elem.group(), sep = "")
        for num, item in enumerate(elem.groups()):
            if item:
                print(num + 1, "/", elem.start(num+1), ": ", item, sep="")

        for key, value in elem.groupdict().items():
            if value:
                print(key, "/", elem.start(key), ": ", value, sep = "")

    else:
        print("<NONE>")

    string = input()

