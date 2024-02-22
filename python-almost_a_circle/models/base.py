#!/usr/bin/python3
import json
"""Write the first class"""


class Base:
    """Write the first class Base"""
    _nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    def to_json_string(list_dictionaries):
        """static method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)
