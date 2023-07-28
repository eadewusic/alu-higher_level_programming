#!/usr/bin/python3
"""This is a python module
that creates a function and returns
an object."""


def lookup(obj):
    """This is a function that takes in a class
    object as a variable and returns a list of it's
    possible attributes, methods (magic methods and self defined methods)
    def lookup(obj):

    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list of attribute and method names as strings.
    """
    return dir(obj)
