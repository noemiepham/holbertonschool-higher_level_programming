#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """appends a string at the end"""
    with open(filename, 'a', encoding="utf-8") as myfile:
        myfile.write(text)
    with open(filename, encoding="utf-8") as countFile:
        i = 0
        for j in range(len(text)):
            i += 1
        return (i)
