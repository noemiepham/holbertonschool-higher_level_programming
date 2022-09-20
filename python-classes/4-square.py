#!/usr/bin/python3
''' python3 -c 'print(__import__("my_module").__doc__)'''


class Square():
    '''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''

    def __init__(self, size=0):
        self.__size = size
        '''python3 -c 'print(__import__("my_module").
          MyClass.my_function.__doc__)'''

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        try:
            if value < 0:
                raise ValueError('size must be >= 0')
            if not isinstance(value, int):
                raise TypeError('size must be an integer')
        except TypeError:
            raise TypeError('size must be an integer')
        self.__size = value
