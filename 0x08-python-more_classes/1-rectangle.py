#!/usr/bin/python3

'''Rectangle class'''


class Rectangle:
    '''An empty class Rectangle'''
    def __init__(self,  height=0, width=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, width):
        '''Set the width of the rectangle'''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        '''get the height of the rectangle'''
        return self.__height

    @height.setter
    def height(self, height):
        '''Set the height of the rectangle'''
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
