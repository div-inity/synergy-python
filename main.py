# 🌲 🌊 🚁 🈯️ 🔥 🏥 ❤️ 🪣 🛒 ☁️ ⚡ 🏆 ⬛️
from map import Map
import time
import os
from helicopter import helicopter as Helico
#from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W,MAP_H)
print(field.w, field.h)
field.generate_forest(3,10)
field.generate_river(10)
field.generate_river(10)

helico = Helico(MAP_W,MAP_H)


def clear_screen():
    os.system('cls || clear')

tick = 1
while True:
    clear_screen()
    print("TICK", tick)
    CELL_TYPES = "🈯️🌲🌊🚑🛒🔥"
    print(CELL_TYPES)
    for i in range(len(CELL_TYPES)):
        print(i, " ", CELL_TYPES[i])
    print()
    field.print_map(helico)
    tick +=1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()