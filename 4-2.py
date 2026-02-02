x = int(input())
n = x
i = 0
while n > 0 :
    if x % n == 0 : i += 1
    n -= 1

print(i)