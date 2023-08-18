#!/usr/bin/python3
"""
This is a python module

that has the class base

This class will be the “base”

of all other classes in this project

The goal of it is to manage id attribute

in all your future classes and to avoid

duplicating the same code (by extension, same bugs)
"""


import json


class Base:
    """
    This class base has the following;

    private class attribute __nb_objects = 0

    class constructor: def __init__(self, id=None):
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization

        constructor method for each

        instance or object of this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.

        the static method def to_json_string(list_dictionaries)

        that returns the JSON string representation of list_dictionaries

        list_dictionaries is a list of dictionaries

        If list_dictionaries is None or empty, return the string: "[]"

        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        the class method def save_to_file(cls, list_objs)

        that writes the JSON string representation of list_objs to a file

        list_objs is a list of instances who inherits of Base

        example: list of Rectangle or list of Square instances

        If list_objs is None, save an empty list

        The filename must be: <Class name>.json - example: Rectangle.json

        You must use the static method to_json_string (created before)

        You must overwrite the file if it already exists
        """
        if list_objs is None:
            data = cls.to_json_string(list_objs)
            data = json.loads(data)
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") \
                    as classfile:
                json.dump(data, classfile)
            return 1
        else:
            new_list_objs = []
            for i in range(len(list_objs)):
                hash_maps = list_objs[i].to_dictionary()
                new_list_objs.append(hash_maps)
            data = cls.to_json_string(new_list_objs)
            data = json.loads(data)
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") \
                    as classfile:
                json.dump(data, classfile)
            return 0

    @staticmethod
    def from_json_string(json_string):
        """
        the static method def from_json_string(json_string)

        that returns the list of the JSON string

        representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        the class method def create(cls, **dictionary)

        that returns an instance with all attributes already set

        **dictionary can be thought of as a double pointer to a dictionary

        To use the update method to assign all attributes,

        you must create a “dummy” instance before

        Create a Rectangle or Square instance with “dummy”

        mandatory attributes (width, height, size, etc.)

        Call update instance method to this “dummy”

        instance to apply your real values

        You must use the method def update(self, *args, **kwargs)

        **dictionary must be used as **kwargs of the method update

        You are not allowed to use eval
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
            update_dummy = dummy.update(**dictionary)
            return dummy
        else:
            dummy = cls(4)
            update_dummy = dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        the class method def load_from_file(cls)

        that returns a list of instances

        The filename must be: <Class name>.json - example: Rectangle.json

        If the file doesn’t exist, return an empty list

        Otherwise, return a list of instances -

        the type of these instances depends on cls

        (current class using this method)

        You must use the from_json_string and

        create methods (implemented previously)
        """
        try:
            with open(f"{cls.__name__}.json", mode="r", encoding="utf-8") \
                    as classfile:
                new_object_list = []
                data = classfile.read()
                data = cls.from_json_string(data)
                for i in range(len(data)):
                    obj_data = data[i]
                    obj = cls.create(**obj_data)
                    new_object_list.append(obj)
                return new_object_list
        except FileNotFoundError:
            return []
