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

    def to_json(self):
        '''Returns a dictionary representation of the student instance
        '''
        return self.__dict__
