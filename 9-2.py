import collections
pets = {
    1:{
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2:{
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def create ():
    last = collections.deque(pets, maxlen=1)[0]
    p_name = input("Введите имя питомца: ")
    p_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    name = input("Введите имя владельца: ")

    pets[last + 1] = {
        p_name : {
            "Вид питомца": p_type,
            "Возраст питомца": age,
            "Имя владельца": name,
        }
    }
    pets_list()

def read():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)
    if not pet_info:
        print(f"Питомец с ID {pet_id} не найден!")
        return
    p_name = list(pet_info.keys())[0]
    pet_data = pet_info[p_name]

    print(f'Это {pet_data["Вид питомца"]} по кличке "{p_name}". '
          f'Возраст питомца: {pet_data["Возраст питомца"]} {get_suffix(pet_data["Возраст питомца"])}. '
          f'Имя владельца: {pet_data["Имя владельца"]}')

def update():
    p_name = input("Введите имя питомца: ")
    pet_info = get_pet_by_name(p_name)
    print(pet_info)
    if pet_info[0] == False:
        print(f"Питомец с именем {p_name} не найден!")
        return

    pets[pet_info[0]][p_name]["Вид питомца"] = input("Введите вид питомца: ")
    pets[pet_info[0]][p_name]["Возраст питомца"] = int(input("Введите возраст питомца: "))
    pets[pet_info[0]][p_name]["Имя владельца"] = input("Введите имя владельца: ")

def delete():
    id = int(input("Введите ID питомца для удаления: "))
    pet_info = get_pet(id)

    if not pet_info:
        print(f"Питомец с ID {id} не найден!")
        return

    pet_name = list(pet_info.keys())[0]
    del pets[id]
    print(f"Питомец {pet_name} (ID: {id}) успешно удален!")

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_pet_by_name(name):
    for id, info in pets.items():
        if name in info:
            return id, info
    return False, False

def get_suffix(age):
    if (age % 10 == 1):
        y = "год"
    elif (age % 10 > 1 and age % 10 < 5):
        y = "года"
    else:
        y = "лет"
    return y

def pets_list():
    print("=" * 50)
    print("Список питомцев:")
    print("=" * 50)

    for i in pets.keys() :
        p_names = list(pets[i].keys())
        p_info = list(pets[i].values())
        index = 0
        for k in p_info:
            print(f'Это {k["Вид питомца"]} по кличке "{p_names[index]}". '
                  f'Возраст питомца: {k["Возраст питомца"]} {get_suffix(k["Возраст питомца"])}. '
                  f'Имя владельца: {k["Имя владельца"]}')
            index += 1

command = ''

while command != 'stop':
    command = input()
    match command:
        case 'create':
            create()
        case 'read':
            read()
        case 'update':
            update()
        case 'delete':
            delete()
        case 'get_pet':
            print(get_pet(int(input("ID питомца: "))))
        case 'pets_list':
            pets_list()
