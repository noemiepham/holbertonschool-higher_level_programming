#!/usr/bin/python3
""" Rectangcle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square"""

    def __init__(self, size):
        """constructor"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Raise Exception"""
        return (self.__size * self.__size)

    def __str__(self):
        return super().__str__()
