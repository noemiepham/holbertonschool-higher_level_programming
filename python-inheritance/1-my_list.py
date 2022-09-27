#!/usr/bin/python3
""" Mylist"""


class MyList(list):
    """ Contains list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
