#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    newarray = []
    for row in matrix:
        squre_itertor = map(lambda i: i ** 2, row)

        newarray.append(list(squre_itertor))
    return newarray