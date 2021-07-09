from collections import UserString

class SubString(UserString):
    def __sub__(self, other):
        import collections
        result = []
        other = collections.Counter(other)
        for c in self:
            if other[c] == 0:
                result.append(str(c))
            else :
                other -= collections.Counter(c)
        result = "".join(result)
        return SubString(result)

del UserString