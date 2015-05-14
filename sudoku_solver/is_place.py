__author__ = 'Deepanshu'

def iinput(my_array, row, col, value):
    for i in range(0, 9):
        if my_array[row][i] == value:
            return False
    for i in range(0, 9):
        if my_array[i][col] == value:
            return False
    logic_row = (row // 3) * 3
    logic_col = (col // 3) * 3
    for i in range(logic_row, logic_row + 3):
        for j in range(logic_col, logic_col + 3):
            if my_array[i][j] == value:
                return False
    return True
