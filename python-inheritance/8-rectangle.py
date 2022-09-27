#!/usr/bin/python3
"""Rectangle"""


class BaseGeometry:
    """class empty"""

    def area(self):
        """Raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check type de value input"""
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """constructor"""
        BaseGeometry.__init__(self)
        bg = BaseGeometry()
        bg.integer_validator(width, height)
