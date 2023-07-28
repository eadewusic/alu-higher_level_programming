#!/usr/bin/python3
"""This is a python script that
creates a class with attributes
and method.
"""


class Rectangle():
    """This is a class that
    has private instance atrributes,
    getters, and setters, and a method
    for initialization.
    """
    def __init__(self, width=0, height=0):
        """This is the initialization
        method for each instance of a class
        and it does some setting methods
        for checks.
        """
        self.width = width
        self.__width = width
        self.height = height
        self.__height = height

    @property
    def width(self):
        """This is the width
        @property for the width
        private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This is the width setter
        or the width private instance
        attribute.
        """
        try:
            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        except TypeError:
            raise
        except ValueError:
            raise

    @property
    def height(self):
        """This is the
        height private instance
        attribute getter.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This is the height
        private instance attribute
        setter method.
        """
        try:
            if type(value) != int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        except TypeError:
            raise
        except ValueError:
            raise
