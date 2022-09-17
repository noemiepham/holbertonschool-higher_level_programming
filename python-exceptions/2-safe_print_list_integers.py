#!/usr/bin/python3
from distutils.log import error
from itertools import count


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    error = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
        except (ValueError, TypeError):
            count += 1
            error += 1
    count -= error
    print()
    return count
