#!/usr/bin/python3
""" function that prints a text with
 2 new lines after each of these characters: ., ? and :"""


from sys import flags
from unittest import skip


def text_indentation(text):
    """ insert doble jump line after . : or ? """

    characters = [".", "?", ":"]
    skip_next = False
    if type(text) != str:
        raise TypeError('text must be a string')
    for letter in text:
        if letter in characters:
            print(letter)
            print()
            skip_next = True
        else:
            if flags is False:
                print(letter, end="")
            else:
                if letter != " ":
                    print(letter, end="")
                    skip_next = False
