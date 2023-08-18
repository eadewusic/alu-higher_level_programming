#!/usr/bin/python3
"""
the class Rectangle that inherits from Base

the file models/rectangle.py

Private instance attributes, each with its own public getter and setter

Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class.

With a setter, you are able to validate what a developer

is trying to assign to a variable.

So after, in your class you can “trust” these attributes.
"""


from models.base import Base


class Rectangle(Base):
    """
    The class rectangle that has the

    Class constructor: def __init__(self, width, height, x=0, y=0, id=None)

    Private instance attributes, each with its own public getter and setter
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __width -> width

        __height -> height

        __x -> x

        __y -> y

        Calls the super class with id - this super call

        with use the logic of the __init__ of the Base class

        Assigns each argument width, height, x and y to the right attribute
        """
        try:
            self.width = width
            self.__width = width
        except Exception as e:
            raise
        try:
            self.height = height
            self.__height = height
        except Exception as e:
            raise
        try:
            self.x = x
            self.__x = x
        except Exception as e:
            raise
        try:
            self.y = y
            self.__y = y
        except Exception as e:
            raise
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"width must be an integer")
            elif value < 1:
                raise ValueError(f"width must be > 0")
            else:
                self.__width = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"height must be an integer")
            elif value < 1:
                raise ValueError(f"height must be > 0")
            else:
                self.__height = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"x must be an integer")
            elif value < 0:
                raise ValueError(f"x must be >= 0")
            else:
                self.__x = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            if type(value) is not int:
                raise TypeError(f"y must be an integer")
            elif value < 0:
                raise ValueError(f"y must be >= 0")
            else:
                self.__y = value
        except TypeError as e:
            raise
        except ValueError as e:
            raise
        except OverflowError as e:
            raise

    def __getattr__(self, name):
        if name == "width":
            pass
        elif name == "height":
            pass
        elif name == "x":
            pass
        elif name == "y":
            pass
        else:
            return None

    def area(self):
        """
        the public method def area(self):

        that returns the area value of the

        Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        the public method def display(self):

        that prints in stdout the Rectangle instance

        with the character #-

        not handling x and y here.

        now taking care of x and y

        in 7.display#1
        """
        shape = ""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            for _ in range(self.x):
                shape += " "
            for _ in range(self.width):
                shape += '#'
            if i != self.height - 1:
                shape += '\n'
        print(shape)
        return 0

    def __str__(self):
        """
        the class Rectangle by overriding the

        __str__ method so that it returns

        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        the public method def update(self, *args):

        that assigns an argument to each attribute

        1st argument should be the id attribute

        2nd argument should be the width attribute

        3rd argument should be the height attribute

        4th argument should be the x attribute

        5th argument should be the y attribute
        """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                else:
                    self.y = args[4]
        else:
            copy_kwargs = dict(kwargs)
            for _ in range(len(kwargs)):
                if "width" in kwargs:
                    self.width = kwargs["width"]
                    del kwargs['width']
                elif "height" in kwargs:
                    self.height = kwargs["height"]
                    del kwargs["height"]
                elif "x" in kwargs:
                    self.x = kwargs["x"]
                    del kwargs["x"]
                elif "y" in kwargs:
                    self.y = kwargs["y"]
                    del kwargs["y"]
                else:
                    self.id = kwargs["id"]
                    del kwargs["id"]
        if len(args) == 0 and len(copy_kwargs) == 0:
            return 1
        else:
            return 0

    def to_dictionary(self):
        """
        the class Rectangle by adding the public method

        def to_dictionary(self)

        that returns the dictionary representation of a Rectangle
        """
        new_dict = {}
        for i in range(len(self.__dict__)):
            if i == 0:
                new_dict["x"] = self.x
            elif i == 1:
                new_dict["y"] = self.y
            elif i == 2:
                new_dict["width"] = self.width
            elif i == 3:
                new_dict["height"] = self.height
            else:
                new_dict["id"] = self.id
        return new_dict
