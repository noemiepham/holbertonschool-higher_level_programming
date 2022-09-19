#!/usr/bin/python3
''' python3 -c 'print(__import__("my_module").__doc__)'''


from glob import escape


class Square():
    '''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''

    def __init__(self, size=0):
        self.__size = size
        '''python3 -c 'print(__import__("my_module").
          MyClass.my_function.__doc__)'''
        try:
            if size < 0:
                raise ValueError('size must be >= 0')
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
        except TypeError:
            raise TypeError('size must be an integer')
