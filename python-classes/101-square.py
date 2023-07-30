#!/usr/bin/python3
'''Defines a Square class'''


class Square:
    '''Square represents an instance of a square shape'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes a new square object

           Args:
                size (int): The size of the square.
        '''
        self.size = size
        self.position = position

    def __str__(self):
        '''
        Print a rapresentation of square using my_print
        '''
        '''
           Prints graphic representaion of square instance
        '''
        if self.size == 0:
            return ("")

        res = "\n" * self.position[1]
        for i in range(self.size):
            res += " " * self.position[0]
            res += "#" * self.size
            if i != self.size - 1:
                res += "\n"
        return res

    def area(self):
        '''
           Computes the area of the square based on the size.

           Returns:
               The value of the area (int).
        '''
        return self.__size ** 2

    @property
    def size(self):
        '''
           Retrieves the value of size
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
           Sets the value of private attribute size
        '''
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
           Retrieves the current position of square instance.

           Returns:
               The value of position.
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
           Sets the value for position and performs type chacks

           Args:
             value (tuple): The position of the square
        '''
        if (
                isinstance(value, tuple) and
                len(value) == 2 and
                all(map(lambda i: (isinstance(i, int) and
                                   i >= 0), value))
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        '''
           Prints graphic representaion of square instance
        '''
        if self.size == 0:
            print("")
            return

        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
