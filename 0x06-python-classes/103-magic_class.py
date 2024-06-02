#!/usr/bin/python3
"""define a magic class"""

import math


class MagicClass:
    """Magic class implementation"""

    def __inti__(self, radius=0):
        """init function for a circle class"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area function"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """not the area"""
        return (2 * math.pi * self.__raduis)
