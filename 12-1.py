class Transport:

   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def output(self):
       print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

class Autobus(Transport):
    pass

h1 = Autobus("Renaul Logan", 180,120)
h1.output()