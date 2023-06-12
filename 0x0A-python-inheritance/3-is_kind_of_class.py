#!/usr/bin/python3
'''This module contains a function that checks whether\
      a object is an instance of a class or an instance\
        of a class that inherit from'''


def is_kind_of_class(obj, a_class):
    '''Return true if match otherwise false'''
    return isinstance(obj, a_class)
