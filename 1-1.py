p_type, age, name = input(), int(input()), input()
y = ""
if (age % 10 == 1) : y = "год"
elif (age % 10 > 1 and age % 10 < 5) : y = "года"
else : y = "лет"
print("Это ", p_type, " по кличке ", name, ". Возраст: ", age, " ", y, sep="")