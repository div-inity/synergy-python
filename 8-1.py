n = int(input()) #Кол-во вводимых животных
pets = dict()
for i in range(n):
    p_name = input("Введите имя питомца: ")
    p_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    name = input("Введите имя владельца: ")

    pets[p_name] = {
        "Вид питомца": p_type,
        "Возраст питомца": age,
        "Имя владельца": name,
    }

def ages (num):
    if (num % 10 == 1):
        y = "год"
    elif (num % 10 > 1 and num % 10 < 5):
        y = "года"
    else:
        y = "лет"
    return y

p_names = list(pets.keys())
p_info = list(pets.values())

for i in range(len(pets)):
    pet_name = p_names[i]
    pet_info = p_info[i]

    print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". '
          f'Возраст питомца: {pet_info["Возраст питомца"]} {ages(pet_info["Возраст питомца"])}. '
          f'Имя владельца: {pet_info["Имя владельца"]}')
