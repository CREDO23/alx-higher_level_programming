#!/usr/bin/python3

"""Implementation of a Square class"""


class Square():
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):

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
        self.__position = position

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

        self.__size = newsize

    def my_print(self):

        if self.size == 0:
            print("")
        for x in range(self.position[1]):
            print("")
        for y in range(self.size):
            for i in range(self.position[0]):
                print(" ", end='')
            for j in range(self.size):
                print("#", end='')
            print("")

    @property
    def position(self):
        """Return the position of the square
        """
        return self.__position

    @position.setter
    def position(self, newpos):
        """set the new position of the Square
        Raises:
            TypeError: if value is not a tuple of two integers
        """
        if not isinstance(newpos, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(newpos) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in newpos if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = newpos
