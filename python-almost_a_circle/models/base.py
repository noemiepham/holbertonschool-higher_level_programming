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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """cls list"""
        with open(cls.__name__ + "j.son", mode="w") as write_file:
            lis = []
            if list_objs is None:
                write_file.write("[]")
            else:
                for item in list_objs:
                    lis.append(item.to_dictionary())
                write_file.write(cls.to_json_string(lis))
