a = int(input())
even, sign, message = "", "", ""
if a > 0 :
    sign = 'положительное'
elif a == 0 :
    sign = 'нулевое'
else :
    sign = 'отрицательное'

if a % 2 != 0:
    even = 'нечетное'
    message = "число не является четным"
else :
    even = "четное"

print(sign, even, "число")
if len(message) != 0:
    print( message)
