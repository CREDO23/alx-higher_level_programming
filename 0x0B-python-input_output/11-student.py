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

        if type(attrs) == list and all(type(el) == str for el in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''Replaces the properties in json'''

        for k, v in json.items():
            setattr(self, k, v)
