#!/usr/bin/python3
"""Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.__width = width
        self.__height = height
        bg = BaseGeometry()
        bg.integer_validator(width, height)
