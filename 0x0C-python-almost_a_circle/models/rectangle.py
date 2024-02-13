#!/usr/bin/python3
'''Module for rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''A rectangle class'''

    def __init__(self, width, height, x, y, id=None):
        '''constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        self.width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        self.height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        self.x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        self.y = value
