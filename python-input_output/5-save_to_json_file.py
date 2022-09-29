#!/usr/bin/python3
"""import module json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text, using JSON"""
    with open(filename, "a") as my_file:
        json_object = json.dumps(my_obj)
        json.loads(json_object)
        my_file.write(json_object)
