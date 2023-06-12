#!/usr/bin/python3

'''This module contains a class that inherits from the list class'''


class MyList(list):
    '''This class implements inherit the list class'''

    def print_sorted(self):
        '''Print the list in sorted order'''
        print(sorted(self))
