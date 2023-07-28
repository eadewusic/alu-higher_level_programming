#!/usr/bin/python3
"""This is module that
that initializes an object using the __init__ method
creates a @property method, and a setter @propertyname.setter
also a method called area to return the area of a square.
"""


class Square():
    """This is a class that initializes
    an object, creates a property method
    a setter method and a public instance method
    """
    def __init__(self, size=0):
        """The initialization method
        for the square class
        """
        self.__size = size

    @property
    def size(self):
        """This is the getter method
        for the private instance attribute __size
        so we directly manipulate the __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This is the setter method
        for the getter size method that helps
        us control how we change the value of
        __size attribute.
        """
        try:
            if not type(value) == int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        except TypeError:
            raise
        except ValueError:
            raise

    def area(self):
        """This returns the Area of the square
        using the size of the square.
        """
        return self.size ** 2

    def my_print(self):
        """This prints out the shape
        of our square based on the size
        given by the user.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("#", end="")
                print()
