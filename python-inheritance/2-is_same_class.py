#!/usr/bin/python3
"""This is a python
module with a function"""


def is_same_class(obj, a_class):
    """This is a function
    testing if an object is
    was created from a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
