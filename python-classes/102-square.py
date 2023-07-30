#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''
    Square represents an instance of a square shape.

    Attributes:
        size (int or float): The size of the square.
    '''

    def __init__(self, size=0):
        '''
        Initializes a new square object.

        Args:
            size (int or float): The size of the square.
        '''
        self.size = size

    def area(self):
        '''
        Computes the area of the square based on the size.

        Returns:
            The value of the area (int or float).
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
        Retrieves the value of size.

        Returns:
            The value of size (int or float).
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the value of private attribute size.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is less than 0.
        '''
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        '''
        Compares two squares for equality based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the areas of both squares are equal, False otherwise.
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        '''
        Compares two squares for inequality based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the areas of both squares are
            not equal, False otherwise.
        '''
        return self.area() != other.area()

    def __lt__(self, other):
        '''
        Compares two squares based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the area of the first square is less than
            the area of the second square, False otherwise.
        '''
        return self.area() < other.area()

    def __le__(self, other):
        '''
        Compares two squares based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the area of the first square is less than
            or equal to the area of the second square, False otherwise.
        '''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''
        Compares two squares based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the area of the first square is greater than
            the area of the second square, False otherwise.
        '''
        return self.area() > other.area()

    def __ge__(self, other):
        '''
        Compares two squares based on their areas.

        Args:
            other (Square): Another Square instance.

        Returns:
            True if the area of the first square is greater than
            or equal to the area of the second square, False otherwise.
        '''
        return self.area() >= other.area()
