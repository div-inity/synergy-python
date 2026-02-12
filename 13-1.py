class Cassa:
    money = 125
    def __init__(self, m=money):
        self.money = m

    def top_up(self, X):
        self.money += X

    def count_1000(self):
        return self.money // 1000

    def take_away(self, X):
        if self.money < X:
            print("В кассе недостаточно денег")
            return
        self.money -= X

m = Cassa()
print("Сумма на счете: ", m.money)
command = ''
while command != 'stop' :
    command = input("Введите команду: ")
    if command == 'top_up':
        c = int(input("На какую сумму будет пополнение? "))
        m.top_up(c)
        print("Сумма на счете: ", m.money)
    elif command == 'count_1000':
        print(m.count_1000())
        print("Сумма на счете: ", m.money)
    elif command == 'take_away':
        c = int(input("Какую сумму Вы хотите снять со счета? "))
        m.take_away(c)
        print("Сумма на счете: ", m.money)
    elif command == 'stop':
        print("Выход из системы")
        break
    else: print("Неизвестная команда")