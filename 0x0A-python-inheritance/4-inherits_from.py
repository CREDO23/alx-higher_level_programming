#!/usr/bin/python3

'''THis module checks for a class\
      that is a subclass of a class directly or indirectly'''


def inherits_from(obj, a_class):
    '''Returns True if obj is a subclass of a_class, False otherwise'''
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
