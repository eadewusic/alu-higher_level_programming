#!/usr/bin/python3
'''New class rectangle inherits from BaseGeometry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''New Rectangle class inherits from BaseGeometry, and represents a
    rectangle'''
    def __init__(self, width, height):
        '''Initializes new Rectangle obj
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Calculates the area of a rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Return info about the Rectangle instance
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
