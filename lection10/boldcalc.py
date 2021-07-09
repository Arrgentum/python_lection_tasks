import re


full_expr = r"((?P<name>[\dA-Za-z_]+) ?= ?)? ?(?P<expr>[+\-*% ]*(([\(\)])?(([\d]+)|[A-Za-z_][\dA-Za-z_]*)[ =+\-\/*%\(\)]*)+)"


def BoldCalc(st):
    for i in st:
        try:
            i = re.sub(r"(?P<na>[A-Za-z_][\dA-Za-z_]*)", r"\g<na>_name", i)
            if re.findall(r"(//)|(\*\*)|([\dA-Za-z_]+\()|(\d\()|([\dA-Za-z_]+ ?= ?\d+\.\d+)", i):
                raise SyntaxError
            name = re.fullmatch(full_expr, i).group("name")
            expr = re.fullmatch(full_expr, i).group("expr")
            # print('name =', name, '; expr =', expr)
            # print(name.isidentifier())
            if name and not name.isidentifier():
                raise AttributeError
            # print(round(eval(i, locals())))
            exec(i, locals())
            #exec(i)
            if '=' not in i:
                i = re.sub(r"/", r"//", i)
                print(eval(i, locals()))
                #print(eval(i))
            # print('---')
        except NameError:
            print('Name error')
        except AttributeError:
            print("Assignment error")
        except (SyntaxError, TypeError):
            print('Syntax error')
        except:
            print('Runtime error')


txt = list()
s = input()
while s:
    if s[0] != '#':
        txt.append(s)
    s = input()
BoldCalc(txt)