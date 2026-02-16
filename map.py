from utils import randbool
from utils import randcell
from utils import randcell2

""" 0 - поле
        2 - дерево
        3 - река
        4 - госпиталь
        5 - магазин
        6 - огонь
    """
CELL_TYPES = "🈯️🌲🌊🚑🛒🔥"

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]


    def print_map(self, helico):
        print("⬛️" * (self.w + 2))
        for ri in range(self.h):
            print("⬛️", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if helico.x == ri and helico.y == ci:
                    print("🚁", end="")
                elif 0 <= cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end="")
            print("⬛️")
        print("⬛️" * (self.w + 2))

    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def generate_river(self, l):
        rc = randcell(self.w, self.h)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 3
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 3
                rx, ry = rx2, ry2
                l -= 1

    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r,mxr):
                    self.cells[ri][ci] = 2

    def generate_tree(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 2

    def add_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 6

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 6:
                    self.cells[ri][ci] = 0
        for i in range(5):
            self.add_fire()


