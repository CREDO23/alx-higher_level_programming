#!/usr/bin/python3


"""A docstring for this mod"""
import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """Initialize the magic"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """the area of the"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """the circumference of the"""
        return 2 * math.pi * self.__radius
