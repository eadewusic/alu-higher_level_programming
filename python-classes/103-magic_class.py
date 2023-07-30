#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode provided."""

import math

class MagicClass:
    """
    MagicClass represents a class that performs circle-related calculations.
    """

    def __init__(self, radius=0):
        """
        Initialize a new MagicClass object with a given radius.

        Args:
            radius (int or float): The radius of the circle (default is 0).

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Compute the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Compute the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
