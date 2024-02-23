#!/usr/bin/python3
"""Write the first class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method"""
        if list_objs is None:
            list_objs = '[]'
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            json_string = json.dumps(dict_list)
            file.write(json_string)
