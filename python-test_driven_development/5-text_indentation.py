#!/usr/bin/python3
""" function that prints a text with
 2 new lines after each of these characters: ., ? and :"""


import string


def text_indentation(text):
    """ text must be a string,
    otherwise raise a TypeError exception with the message
    text must be a string """
    if type(text) != str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i - 1] == "." or text[i - 1] == '?' or text[i - 1] == ":":
            print()
        else:
            print(text[i], end="")
    print()
