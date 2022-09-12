#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        newlist = [x for x in matrix[row]]
        for i in range(len(newlist)):
            print("{:d} ".format(newlist[i]), end="")
        print()
