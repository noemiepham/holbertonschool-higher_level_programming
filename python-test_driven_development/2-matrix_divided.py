#!/usr/bin/python3
""" matrix_divided divides the given matrix
by the parameter "div", and returns the divided matrix
"""


def matrix_divided(matrix, div):
    
    """ Divides all elements of a matrix by "div"
    checks if the entire list is int/float
    checks if each list in the matrix are the same size
    checks if "div" is an int/float or is 0
    """

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
