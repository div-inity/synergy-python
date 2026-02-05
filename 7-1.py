n = int(input())
m = list(map(int, input().split()))
if len(m) > n : # Удаление лишнего
    del m[n:]

p = set(m)
print(len(p))
