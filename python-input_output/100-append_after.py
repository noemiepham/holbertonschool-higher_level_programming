#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append line after search"""
    with open(filename, "r+", encoding="UTF8") as read_file:
        temp = read_file.readlines()
    count = 0
    with open(filename, "w", encoding="UTF8") as write_file:
        for lines in temp:
            count += 1
            if search_string in lines:
                temp.insert(count, new_string)
        for lines in temp:
            write_file.write(lines)
