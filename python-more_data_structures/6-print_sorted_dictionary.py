#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = sorted(a_dictionary.items())
    for keys, Values in a_dictionary:
        print("{}: {}".format(keys, Values))
