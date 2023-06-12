#!/usr/bin/python3

'''This module contains a class that inherits from the list class'''


class MyList(list):
    '''This class implements inherit the list class'''

    def __init__(self):
        '''Intialize the class'''
        super().__init__(self)

    def print_sorted(self):
        '''Print the list in sorted order'''
        print(sorted(self))
