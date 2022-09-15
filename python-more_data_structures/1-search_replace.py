#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = [element for element in my_list]
    for item in newlist:
        if newlist[item] == search:
            newlist[item] = replace
        return newlist

    # method2: newlist = [replace
    # if item == search else item for item in my_list ]
    # return newlist
