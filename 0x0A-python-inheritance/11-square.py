#!/usr/bin/python3
'''This module contains the Square class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''This is the Square class'''

    def __init__(self, size):
        '''Initialises the Square class'''
        self.integer_validator("size", size)
        super().__init__(width=size, height=size)
        self.__size = size

    def __str__(self):
        '''Print the square class as str'''
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
