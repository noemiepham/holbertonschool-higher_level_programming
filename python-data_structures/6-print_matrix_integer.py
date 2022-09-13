#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        array = matrix[row]
        lenArray = len(array)
        for idx in range(lenArray):
            if idx != lenArray - 1:
                print("{:d}".format(array[idx]), end=" ")
            else:
                print("{:d}".format(array[idx]))
