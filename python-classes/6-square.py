#!/usr/bin/python3
''' python3 -c 'print(__import__("my_module").__doc__)'''


class Square():
    '''python3 -c 'print(__import__("my_module").MyClass.__doc__)'''

    # Instantiation with optional size and optional position
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        self.__size = size
        '''python3 -c 'print(__import__("my_module").
          MyClass.my_function.__doc__)'''

    # Private instance attribute: size
    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    # Private instance attribute: position
    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        self.__position = value

    # Function
    def area(self):
        return (self.__size * self.__size)

    # Public instance method
    def my_print(self):
        countSpace = self.__position[0]
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for y in range(self.size):
            self.value = "#"
            self.position = ' '
            print(self.position * countSpace + (self.value * self.__size))
