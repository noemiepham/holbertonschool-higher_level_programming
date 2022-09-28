#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """Creat and write on file"""
    with open(filename, 'w+', encoding="utf-8") as myfile:
        myfile.write(text)
    myfile = open(filename, "r")
    i = 0
    for j in range(len(myfile.read())):
        i += 1
    return (i)
