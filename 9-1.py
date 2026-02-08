def factorial (n) :
    a = 1
    for i in range(1, n+1) :
        a *= i
    return a

p = factorial(3)
f = list()
for i in range(p, 0, -1):
    f.append(factorial(i))

print(f)