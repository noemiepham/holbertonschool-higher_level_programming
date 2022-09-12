#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{}".format(i), end=" ")
        print()

    # for row in range(len(matrix)):
    #      newlist = matrix[row]
    #      for i in range(len(newlist)):
    #          print("{}".format(newlist[i]), end="")
    #      print()
