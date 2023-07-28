#!/usr/bin/python3
'''Defines class Square
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class represents a square
    '''
    def __init__(self, size):
        '''Initializes a new Square object
        '''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''Returns a string with info on the square
        '''
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        '''Calculates the area of a Square object
        '''
        return self.__size ** 2
