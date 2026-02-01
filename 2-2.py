num = int(input())
a = num // 10000 % 10
b = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
e = num % 10
n = float(d ** e * c // (a - b))
print(n)