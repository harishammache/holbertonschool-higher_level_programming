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
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """static method """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class methode"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class methode """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(json_data)
        instance_list = []
        for dictionary in dict_list:
            instance = cls.create(**dictionary)
            instance_list.append(instance)

        return instance_list
