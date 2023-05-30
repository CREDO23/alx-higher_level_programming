#!/usr/bin/python3

"""Implementation of a Square class"""


class Square():
    """Defines a square"""
    def __init__(self, size=0):

        """Initializing this square class
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, newsize):
        """Set the size of the square"""
        if not isinstance(newsize, int):
            raise TypeError('size must be an integer')
        if newsize < 0:
            raise ValueError('size must be >= 0')
