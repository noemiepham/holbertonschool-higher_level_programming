#!/usr/bin/python3
"""class parents"""
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON"""
        temp = {}
        if list_dictionaries is None:
            return "[]"
        else:
            json.dumps(list_dictionaries)
