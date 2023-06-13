#!/usr/bin/python3
'''THis module contains a Student class'''


class Student():
    '''The student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize the Student'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Return the Student json representation (dict)'''
        return self.__dict__
