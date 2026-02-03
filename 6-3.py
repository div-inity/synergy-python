m = int(input()) # максимальная масса
n = int(input()) # количество рыбаков
s = [] # вес каждого
count = 0 # кол-во лодок
for i in range(n) :
    s.append(int(input()))

s.sort()

left = 0
right = n - 1

while left <= right :
    if left == right :
        count += 1
        break

    if s[left] + s[right] <= m :
        left += 1
        right -= 1
    else :
        right -= 1

    count += 1

print(count)