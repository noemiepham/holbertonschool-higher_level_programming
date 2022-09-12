#!/usr/bin/python3
import numbers


def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return
    else:
        list = my_list[::-1]
        for i in list:
            if i in range(0, 10):
                print("{:d}".format(i))
            else:
                break
