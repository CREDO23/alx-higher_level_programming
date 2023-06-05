#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    '''An empty class Rectangle'''
    def __init__(self, width=0, height=0):
        '''Initializes a new Rectangle'''
        self.width = width
        self.height = height

    @property
    def height(self):
        '''get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, h):
        '''Set the height of the rectangle'''
        if not isinstance(h, int):
            raise TypeError('height must be an integer')
        if h < 0:
            raise ValueError('height must be >= 0')
        self.__height = h

    @property
    def width(self):
        '''Get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, w):
        '''Set the width of the rectangle'''
        if not isinstance(w, int):
            raise TypeError('width must be an integer')
        if w < 0:
            raise ValueError('width must be >= 0')
        self.__width = w

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    
    def __str__(self) -> str:
        """Represent the clas a a string"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
