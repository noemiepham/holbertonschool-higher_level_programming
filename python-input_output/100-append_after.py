#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append line after search"""
    with open(filename, "w+", encoding="UTF8") as my_file:
        for i in my_file.readlines():
            print(i)
            if search_string in i:
                print(search_string)

