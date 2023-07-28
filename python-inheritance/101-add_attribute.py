#!/usr/bin/python3
'''Tries to add an attribute to an object
'''


def add_attribute(obj, name, value):
    '''add_attribute tries to add an attribute to an obj
    Args:
       obj (Any object type): The object instance to add attributes to
       name (string): The name of the attribute to set.
       value (any obj type): The value to be stored.
    '''
    if not hasattr(obj, "__dict__") or hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
