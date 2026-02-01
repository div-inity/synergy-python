s = []
for i in range(6):
    s.append(input(f"Введите стадию развития человека № {i+1}: "))
print(*s, sep="->")