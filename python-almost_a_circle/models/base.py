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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON"""
        if list_dictionaries is None:
            return "[]"
        else:
            json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_str):
        if type(json_str) != str:
            return []
        return json.load(json_str)

