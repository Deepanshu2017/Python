__author__ = 'Deepanshu'

import preety_print
import solver

if __name__ == '__main__':
    my_array = [[0 for i in range(0, 9)] for j in range(0, 9)]
    #Now giving default sudoku but soon replace it with GUI input
    """
    my_array = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
    """
    print()
    preety_print.pprint(my_array)
    print()
    print('*' * 37)
    print()
    solver.solve(my_array, 0, 0)


