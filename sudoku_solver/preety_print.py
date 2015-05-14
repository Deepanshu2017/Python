__author__ = 'Deepanshu'


def pprint(my_array):
    print('-' * 37)
    for i in range(0, 9):
        print('| ', end='')
        for j in range(0, 9):
            print(my_array[i][j], "| ", end='')
        print()
    print('-' * 37)

