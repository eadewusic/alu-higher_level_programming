#!/usr/bin/python3
'''Defines class student
'''


class Student:
    '''Represents user data of a student
    '''
    def __init__(self, first_name, last_name, age):
        '''Initializes a new student inatsnce
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns a dictionary representation of the student instance
        '''
        if type(attrs) == list and all(map(lambda x: type(x) == str, attrs)):
            return {key: self.__dict__[key]
                    for key in self.__dict__.keys() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        '''Replaces all attributes of a student instance
        '''
        for k, v in json.items():
            setattr(self, k, v)
