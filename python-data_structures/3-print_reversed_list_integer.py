#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return
    else:
        i = len(my_list)
        while (i > 0):
            print("{:d}".format(i))
            i -= 1
