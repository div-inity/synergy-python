import random
w = int(input("Введите ширину матрицы: "))
h = int(input("Введите высоту матрицы: "))
matrix_1 = [[random.randint(1, 10) for b in range(w)] for i in range(h)]
matrix_2 = [[random.randint(1, 10) for b in range(w)] for i in range(h)]
matrix_3 = [[0 for a in range(w)] for b in range(h)] #Итоговая матрица

print("Матрица matrix_1:")
for i in range(h):
    print(matrix_1[i])

print("Матрица matrix_2:")
for i in range(h):
    print(matrix_2[i])
def sum():
    for i in range(h) :
        for j in range(w):
            matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
        print(matrix_3[i])
print("Матрица matrix_3:")
sum()