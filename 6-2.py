n = int(input())
m = [int(input()) for i in range(n)]

class ar:
    def __init__(self, val):
        self.val = val

    def edit(self):
        e = self.val
        e = [e[-1]] + e[:-1]
        return e

a = ar(m)
print(a.edit())