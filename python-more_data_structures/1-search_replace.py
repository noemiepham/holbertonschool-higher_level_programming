#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
        newlist.append(my_list[i])
    return newlist
