#!/usr/bin/python3
"""append_write"""


def append_write(filename="", text=""):
    """appends a string at the end"""
    with open(filename, 'a', encoding="utf-8") as myfile:
        myfile.write(text)
    myfile = open(filename, "r")
    i = 0
    for j in range(len(myfile.readline())):
        i += 1
    return (i)
