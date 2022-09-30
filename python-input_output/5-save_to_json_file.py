#!/usr/bin/python3
"""import module json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text, using JSON"""
    with open(filename, "w", encoding="UTF-8") as my_file:
        json.dump(my_obj, my_file)
