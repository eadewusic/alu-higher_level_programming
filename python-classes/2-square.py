#!/usr/bin/python3
# 2-square.py
"""This is a module that
defines a python class called Square
but does some extra work.
"""


class Square():
    """
    a class Square that defines a square by:
    (based on 1-square.py) with a private instance
    attribute called size.
    """
    def __init__(self, size=0):
        """
        instantiate the instance or object
        with the instance private variable
        called __size which is assigned to
        the parameter size in the initialization
        method but some checks are made.

        1. size must be an integer, otherwise
        raise a TypeError exception with the message
        size must be an integer.

        2. if size is less than 0, raise a ValueError
        exception with the message size must be >= 0.
        """
        try:
            if not type(size) == int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise
        except ValueError:
            raise
