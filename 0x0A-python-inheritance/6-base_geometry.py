#!/usr/bin/python3

'''This cmodule contains the BaseGeometry class'''


class BaseGeometry:
    '''The BaseGeometry'''
    def area(self):
        raise Exception('area() is not implemented')
