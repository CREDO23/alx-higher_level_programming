#!/usr/bin/python3
"""Inheris from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Returns the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''Prints the rectangle'''
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
