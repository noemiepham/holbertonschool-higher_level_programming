#!/usr/bin/python3
""" Write a function that prints a square with the character #."""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer
    check size > 0 or size is int or not
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    else:
        i = 0
        while i < size:
            print(size * "#")
            i += 1
