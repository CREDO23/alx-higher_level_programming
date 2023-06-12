#!/usr/bin/python3
'''This module contains the Myint class inherits from int'''


class MyInt(int):
    '''Myint class inherits from int'''
    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return self.real == value
