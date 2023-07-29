#!/usr/bin/python3
'''
Defines new class
'''


class LockedClass:
    '''Class: LockedClass does not allow the user to create instance attributes,
       except for 'first_name'.
    '''
    __slots__ = ['first_name']
