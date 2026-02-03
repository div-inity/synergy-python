n = int(input())
m = []
for i in range(n) :
    m.append(int(input()))

m.reverse()
print(*m)