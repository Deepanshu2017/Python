__author__ = 'Deepanshu'

import is_place
import preety_print

def solve(my_array, row, col):
    if row == 9 and col == 0:
        preety_print.pprint(my_array)
        exit(0)
    else:
        if my_array[row][col]:
            if col >= 8:
                solve(my_array, row + 1, 0)
            else:
                solve(my_array, row, col + 1)
        else:
            for i in range(1, 10):
                if is_place.iinput(my_array, row, col, i):
                    my_array[row][col] = i
                    if col >= 8:
                        solve(my_array, row + 1, 0)
                    else:
                        solve(my_array, row, col + 1)
                    my_array[row][col] = 0


