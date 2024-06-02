#!/usr/bin/python3
"""define a magic class"""

import math


class MagicClass:
    """Magic class implementation"""

    def __init__(self, raduis=0):
        """init function for a circle class"""
        if type(raduis) is not int and type(raduis) is not float:
            raise TypeError("raduis must be a number")
        self.__raduis = raduis

    def area(self):
        """area function"""
        return (self.__raduis ** 2 * math.pi)

    def circumference(self):
        """not the area"""
        return (2 * math.pi * self.__raduis)
