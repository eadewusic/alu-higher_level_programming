#!/usr/bin/python3
"""This is a class module
that creates a class called Square."""


class Square:
    """This is the class Square
    that has a private instance method
    private instance method are created
    with __attribute(variable)name
    """
    def __init__(self, size):
        """
        this is a built-in special python
        function that help instantiate object/
        instance of class variables it is also
        called an initialization method
        """
        self.__size = size
