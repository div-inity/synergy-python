class Torttle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0 :
            print("Количество клеток перемещения не может быть меньше 1")
            return
        self.s -= 1

    def count_moves(self, x2, y2):
        d_x = abs(x2 - self.x) # abs - Движение может быть в отрицательную сторону
        d_y = abs(y2 - self.y)
        moves_x = (d_x + self.s - 1) // self.s
        moves_y = (d_y + self.s - 1) // self.s
        return moves_x + moves_y

    def place(self):
        print(f'Черепашка находится в клетке: {self.x}, {self.y}')

m = Torttle()
command = ''
while command != 'stop' :
    m.place()
    command = input("Введите команду: ")
    if command == 'go_up': m.go_up()

    elif command == 'go_down': m.go_down()

    elif command == 'go_left': m.go_left()

    elif command == 'go_right': m.go_right()

    elif command == 'evolve': m.evolve()

    elif command == 'degrade': m.degrade()

    elif command == 'count_moves':
        x = int(input("Введите координатy x: "))
        y = int(input("Введите координатy y: "))
        print(f'От точки x={m.x}, y={m.y} до точки x={x}, y={y} можно дойти с шагом {m.s} за {m.count_moves(x, y)} шагов')
    elif command == 'stop':
        print("Выход из системы")
        break
    else: print("Неизвестная команда")
