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

    @property
    def position(self):
        """returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of this Square
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """returns the area of the square
        """
        return self.__size * self.__size

    def p_pos(self):
        """returns the position of the square"""
        pos = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            pos += "\n"
        for y in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square with position"""
        print(self.p_pos(), end='')
