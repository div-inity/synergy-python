my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def test(i=0):
    if i >= len(my_list) :
        print("Конец списка")
        return
    print(my_list[i])
    test(i + 1)

test()