#!/usr/bin/python3
"""
Define a real rectangle class
"""


class Rectangle:
    """Representation of rectangles"""
    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height*self.__width

    def perimeter(self):
        """calculate the per of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        """returns the printable string of the rec"""
        str = ""
        if self.__width != 0 and self.__height != 0:
            str += "\n".join("#" * self.__width
                             for j in range(self.__height))
        return str

    def __repr__(self):
        """return a string representation of the rec"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
