#!/usr/bin/python3
''' python3 -c 'print(__import__("my_module").__doc__)'''


def matrix_divided(matrix, div):
    '''python3 -c 'print(__import__("my_module").my_function.__doc__)'''
    message1 = 'matrix must be a matrix (list of lists) of integers/floats'
    message2 = 'Each row of the matrix must have the same size'
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    newrs = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(message1)
        if len(row) != len(matrix[0]):
            raise TypeError(message2)
        inner_list = []
        for items in row:
            if not isinstance(items, (int, float)):
                raise TypeError(message1)
            else:
                rs = round(items / div, 2)
                inner_list.append(rs)
        newrs.append(inner_list)
    return (newrs)
