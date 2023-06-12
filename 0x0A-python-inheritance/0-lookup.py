#!/usr/bin/python3
'''This module contains a function \
      that looks up for attributes and methods inside a class'''


def lookup(obj):
    '''Returns a list of attributes and methods of the given object(obj)'''
    return dir(obj)
