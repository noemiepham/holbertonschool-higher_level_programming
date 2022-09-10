#!/usr/bin/python3
from tkinter import N


def remove_char_at(str, n):
    lenStr = len(str)
    newstr = ""
    if lenStr <= n or n < 0:
        return str
    else:
        for i in range(lenStr):
            if i != n:
                newstr = newstr + str[i]
        return newstr
