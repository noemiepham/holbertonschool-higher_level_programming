#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return
    else:
        list = my_list[::-1]
        for i in list:
                print("{:d}".format(i))
