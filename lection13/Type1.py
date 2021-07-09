from functools import wraps
import inspect

class checked(type):
    def __init__(self, name, parents, Dict):
        for attr, obj in Dict.items():
            if callable(obj) and attr[0-1] != "__":
                setattr(self, attr, confim(obj, attr))
        return super().__init__(name, parents, Dict)


def confim(fun, name):
    info = inspect.getfullargspec(fun)
    pos_or_key, pos, named, keyword = info.args[1:], info.varargs, info.varkw, info.kwonlyargs
    sig = inspect.signature(fun)
    @wraps(fun)
    def newfunction(self, *args, **kwargs):
        bind, dhelp = sig.bind(self, *args, **kwargs), sig.parameters  
        dict1, ind, bool1 = {}, 0, False

        if sig.return_annotation != sig.empty:
            if not isinstance(fun(self, *args, **kwargs), sig.return_annotation):
                raise TypeError(f"Type mismatch: return")
        
        for key, attr in bind.arguments.items():
            if sig.parameters[key].annotation is not sig.empty:
                dict1[key] = [attr, sig.parameters[key]]
        for i in pos_or_key:
            if i in dict1 and not isinstance(args[ind], dict1[i][1].annotation):
                raise TypeError(f"Type mismatch: {i}")
            if ind + 1 >= len(args):
                bool1 = True
                break
            else:
                ind += 1 

        if bool1 == False:
            if pos in dict1:
                for i in args[ind:]:
                    if not isinstance(i, dict1[pos][1].annotation):
                        raise TypeError(f"Type mismatch: {pos}")
            if named in dict1:
                for i in kwargs:
                    if not isinstance(kwargs[i], dict1[named][1].annotation):
                        raise TypeError(f"Type mismatch: {named}")
            for i in keyword:
                if i in dict1 and not isinstance(kwargs[i], dict1[i][1].annotation):
                    raise TypeError(f"Type mismatch: {i}")

        if bool1 == True:
            number = 0
            for i in kwargs:
                if i in dict1 and not isinstance(kwargs[i], dict1[i][1].annotation):
                    raise TypeError(f"Type mismatch: {i}")
                elif i == pos and not isinstance(kwargs[i], dhelp[pos].annotation):
                    raise TypeError(f"Type mismatch: {pos}")
                if number == len(pos_or_key[ind + 1:]) + len(keyword) - 1:
                    break
                number += 1
            for i in kwargs:        
               	if not isinstance(kwargs[i], dict1[named][1].annotation):
                    raise TypeError(f"Type mismatch: {named}")

        #if sig.return_annotation != sig.empty:
        #    if not isinstance(fun(self, *args, **kwargs), sig.return_annotation):
        #        raise TypeError(f"Type mismatch: return")

        return fun(self, *args, **kwargs)
    return newfunction


class E(metaclass=checked):
    def __init__(self, var: int):
        self.var = var if var%2 else str(var)

    def mix(self, val: int, opt) -> int:
        return self.var*val + opt

    def al(self, c: int, d:int=1, *e:int, f:int=1, **g:int):
        return self.var*d

e1, e2 = E(1), E(2)
code = """
e1.mix("q", "q")
e1.mix(2, 3)
e2.mix(2, "3")
e1.al("q")
e1.al(1, 2, 3, 4, 5, 6, foo=7, bar=8)
e2.al(1, 2, 3, 4, 5, 6, foo=7, bar=8)
e1.al("E", 2, 3, 4, 5, 6, foo=7, bar=8)
e1.al(1, "E", 3, 4, 5, 6, foo=7, bar=8)
e1.al(1, 2, "E", 4, 5, 6, foo=7, bar=8)
e1.al(1, 2, 3, "E", 5, 6, foo="7", bar=8)
e1.al(1, f="E", d=1)
e1.al(1, f=1, d="E")
e1.al(1, f="E", d="1")
e1.al(1, d="E", f="1")
e1.al(1, e="E")
e1.al(1, g="E")
"""

for c in code.strip().split("\n"):
    try:
        res = eval(c)
    except TypeError as E:
        res = E
    print(f"Run: {c}\nGot: {res}")