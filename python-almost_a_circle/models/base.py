#!/usr/bin/python3
"""class parents"""
import json
import os


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
        filename = (cls.__name__ + ".json")
        with open(filename, mode="w") as write_file:
            lis = []
            if list_objs is None:
                write_file.write(cls.to_json_string(lis))
            else:
                for item in range(len(list_objs)):
                    lis.append(list_objs[item].to_dictionary())
                write_file.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes"""
        if cls.__name__ == "Rectangle":
            temp = cls(3, 2)
        if cls.__name__ == "Square":
            temp = cls(9)
        # update temp with obj func update()
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Loads from csv file
        """
        class_name = []
        if not os.path.exists(cls.__name__ + ".json"):
            return class_name
        with open(cls.__name__ + ".json", mode="r") as read_file:
            s = read_file.read()
            s_list = cls.from_json_string(s)
            for item in s_list:
                # formatting with create()
                class_name.append(cls.create(**item))
            return class_name
