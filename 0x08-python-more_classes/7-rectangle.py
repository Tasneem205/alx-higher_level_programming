#!/usr/bin/python3
"""
Define a real rectangle class
"""


class Rectangle:
    """Representation of rectangles"""

    number_of_instances = 0
    '''int: thte number of active instances'''

    print_symbol = '#'
    '''type: print symbol, can be any type'''

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """return a string representation of the rec"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """del a rec"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
