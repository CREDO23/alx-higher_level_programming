#!/usr/bin/python3
"""my square module."""


class Square:
    """define a Square."""

    def __str__(self):
        """teach python to print the square my way"""
        return self.p_pos()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """ initialize the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size of square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square  (a tuple of 2 integers)
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ return the area of the square
        """
        return self.__size * self.__size

    def p_pos(self):
        """returns the printed square """
        pos = ""
        if not self.size:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print square."""
        print(self.p_pos(), end="")