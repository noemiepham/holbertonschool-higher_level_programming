#!/usr/bin/python3
"""Presentation of an object"""
import json


def to_json_string(my_obj):
    """return json"""
    return json.dumps(my_obj)

    # chuyển một python object sang string json, dùng hàm dumps
