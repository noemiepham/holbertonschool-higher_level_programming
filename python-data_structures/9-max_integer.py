#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    for idx in range(len(my_list)):
        max = my_list[idx]
        if idx == len(my_list) - 1:
            return max
        elif max > my_list[idx + 1]:
            return max
