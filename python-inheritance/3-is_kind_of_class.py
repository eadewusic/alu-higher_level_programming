#!/usr/bin/python3
"""This is a python module
that has a function in it
to check an object class or
inherited class.
"""


def is_kind_of_class(obj, a_class):
    """The function that returns true
    if the object is an instance of,
    or if the objet is an instance of
    a class that inherited the specified class
    otherwise false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
