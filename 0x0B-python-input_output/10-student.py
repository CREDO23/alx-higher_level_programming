#!/usr/bin/python3
'''THis module contains a Student class'''


class Student():
    '''The student class'''

    def __init__(self, first_name, last_name, age):
        '''Initialize the Student'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Return the Student json representation (dict)'''

        if isinstance(attrs, list) and len(attrs) > 0:

            new_dict = {}

            for k in attrs:
                if k in self.__dict__:
                    new_dict[k] = self.__dict__[k]

            return new_dict
        else:
            return self.__dict__
