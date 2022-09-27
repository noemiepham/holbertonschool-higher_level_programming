#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """check obj is an instanc a class that inherited"""
    if type(obj) != a_class:
        return True
