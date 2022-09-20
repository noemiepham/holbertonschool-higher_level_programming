#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if value < 0:
            raise TypeError('size must be >= 0')
        if not isinstance(value, int):
            raise ValueError('size must be an integer')

        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if type(value) != 'tuple' or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for item in value:
            if not isinstance(item, int) or item < 0:
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
        self.__position = value
