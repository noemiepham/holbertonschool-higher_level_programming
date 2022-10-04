#!/usr/bin/python3
"""import module Rectangle"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inheritance de Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """inherited of Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return  value"""
        return "[Square] ({:d}) {:d}/{:d} - " \
               "{:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update args"""

    def update(self, *args, **kwargs):
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()
