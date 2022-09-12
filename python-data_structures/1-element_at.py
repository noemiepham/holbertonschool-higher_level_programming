#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return 0
    if idx > len(my_list):
        return 0
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
