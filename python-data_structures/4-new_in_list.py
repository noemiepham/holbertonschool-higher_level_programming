#!/usr/bin/python3
from hashlib import new


def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = [element for element in my_list]
        for i in new_list:
            if i == idx:
                tmp = new_list[i]
                new_list[i] = element
                element = tmp
        return new_list
