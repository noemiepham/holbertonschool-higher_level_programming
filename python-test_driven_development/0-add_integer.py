#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").__doc__)'''


from tkinter import filedialog


def add_integer(a, b=98):
    '''python3 -c 'print(__import__("my_module").my_function.__doc__)'''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError('a must be integer')
    elif type(b) != int:
        raise TypeError('b must be integer')
    else:
        return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
