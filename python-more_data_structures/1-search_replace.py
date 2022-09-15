#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # newlist = [element for element in my_list]
    # for item in newlist:
    #    if item == search:
    #       item = replace
    #   return newlist

    newlist = [replace if item == search else item for item in my_list]
    return newlist
