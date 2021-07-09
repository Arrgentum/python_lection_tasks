
class Spiral:

    def right(self, number, index):
        for i in range(number):
            if self.slen < index + i + 1:
                return
            self.curr[0] += 1
            self.art[self.curr[1]][self.curr[0]] = self.s[index + i]
        return self.up(number + 1, index + number)

    def up(self, number, index):
        for i in range(number):
            if self.slen < index + i + 1:
                return
            self.curr[1] += 1
            self.art[self.curr[1]][self.curr[0]] = self.s[index + i]
        return self.left(number + 1, index + number)

    def left(self, number, index):
        for i in range(number):
            if self.slen < index + i + 1:
                return
            self.curr[0] -= 1
            self.art[self.curr[1]][self.curr[0]] = self.s[index + i]
        return self.down(number + 1, index + number)

    def down(self, number, index):
        for i in range(number):
            if self.slen < index + i + 1:
                return
            self.curr[1] -= 1
            self.art[self.curr[1]][self.curr[0]] = self.s[index + i]
        return self.right(number + 1, index + number)

    def __init__(self, str):
        self.d = {}
        for item in str:
            if item in self.d:
                self.d[item] += 1
            else:
                self.d[item] = 1

    def __add__(self, other):
        qwe = Spiral("")

        a = list(self.d.keys())
        for item in other.d.keys():
            if item not in a:
                a.append(item)

        for key in a:
            if key in self.d and key in other.d:
                qwe.d[key] = self.d[key] + other.d[key]
            elif key not in self.d:
                qwe.d[key] = other.d[key]
            else:
                qwe.d[key] = self.d[key]
        return qwe

    def __sub__(self, other):
        qwe = Spiral("")
        for key in self.d:
            if key not in other.d:
                qwe.d[key] = self.d[key]
                continue
            if self.d[key] >= other.d[key]:
                qwe.d[key] = self.d[key] - other.d[key]
            else:
                qwe.d[key] = 0
        return qwe

    def __mul__(self, other):
        qwe = Spiral("")
        for key in self.d:
            qwe.d[key] = self.d[key] * other
        return qwe

    def __str__(self):

        self.s = []
        for key in self.d:
            self.s.append(self.d[key] * key)
        self.s = "".join(self.s)

        hup = 0
        hdown = 0
        lleft = 0
        lright = 0
        k = 1
        sum = 1
        self.slen = len(self.s)
        cur = [0, 0]

        while sum < self.slen:
            cur[0] += min(k, self.slen - sum)
            if cur[0] > lright:
                lright = cur[0]
            sum += k
            if sum >= self.slen:
                break
            k += 1

            cur[1] += min(k, self.slen - sum)
            if cur[1] > hup:
                hup = cur[1]
            sum += k
            if sum >= self.slen:
                break
            k += 1

            cur[0] -= min(k, self.slen - sum)
            if cur[0] < lleft:
                lleft = cur[0]
            sum += k
            if sum >= self.slen:
                break
            k += 1

            cur[1] -= min(k, self.slen - sum)
            if cur[1] < hdown:
                hdown = cur[1]
            sum += k
            if sum >= self.slen:
                break
            k += 1

        self.art = [[" " for _ in range(lright - lleft + 1)] for __ in range(hup - hdown + 1)]
        self.art[-hdown][-lleft] = self.s[0]
        self.curr = [-lleft, -hdown]
        i = 1
        index = 1

        self.right(i, index)            #

        self.art.reverse()

        GREATSTRING = ""
        for item in self.art:
            GREATSTRING += "".join(item) + "\n"
        return GREATSTRING[:-1]

    def __iter__(self):
        for key in self.d:
            for item in list(self.d[key] * key):
                yield item

