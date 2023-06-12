#!/usr/bin/python3
'''This module contains a\
      function which chech if an object is an exact match of a class'''


def is_same_class(obj, a_class):
    '''Return true if obj is an\
          exact match of a class a_class otherwise False'''
    return type(obj) == a_class
