#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdict = dict(a_dictionary)
    for key in newdict:
        newdict[key] *= 2
    return newdict
