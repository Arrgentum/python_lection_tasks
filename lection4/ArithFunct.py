def SUB(a,b):
    if callable(a) or callable(b):
        if callable(a) and callable(b):
            def newsub(x):
                return a(x) - b(x)
            return newsub
        elif callable(a):
            def newsub(x):
                return a(x) - b
            return newsub
        elif callable(b):
            def newsub(x):
                return a - b(x)
            return newsub 
    else:
        return a - b

def DIV(a,b):
    if callable(a) or callable(b):
        if callable(a) and callable(b):        
            def newdiv(x):
                return a(x) / b(x)
            return newdiv
        elif callable(a):
            def newdiv(x):
                return a(x) / b
            return newdiv
        elif callable(b):
            def newdiv(x):
                return a / b(x)
            return newdiv 
    else:
        return a / b

def MUL(a, b):
    if callable(a) or callable(b):
        if callable(a) and callable(b):
            def newmul(x):
                return a(x) * b(x)
            return newmul
        elif callable(a):
            def newmul(x):
                return a(x) * b
            return newmul
        elif callable(b):
            def newmul(x):
                return b(x) * a
            return newmul
    else:
        return a * b

def ADD(a, b):
    if callable(a) or callable(b):
        if callable(a) and callable(b):
            def newadd(x):
                return a(x) + b(x)
            return newadd
        if callable(a):
            def newadd(x):
                return a(x) + b
            return newadd
        if callable(b):
            def newadd(x):
                return b(x) + a
            return newadd
    else:
        def newadd(x):
            return a+b
        return newadd
