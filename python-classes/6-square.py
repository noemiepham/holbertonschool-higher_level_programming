#!/usr/bin/python3
""" Print square division with position"""


from email import message


class Square():
    """a class Square that defines a square by: (based on 5-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """ Size : size the list
            position of square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError('size must be >= 0')
        elif type(value) != int:
            raise TypeError('size must be an integer')
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        message = 'position must be a tuple of 2 positive integers'
        if type(value) != tuple or len(value) != 2:
            raise TypeError(message)

        for item in value:
            if type(item) != int or item < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):

        if self.__size == 0:
            print()

        for newlines in range(self.__position[1]):
            print()

        for row in range(self.__size):
            print((' ' * self.__position[0]) + ('#' * self.__size))
