#!/usr/bin/python3
'''Defines function class_to_json
'''


def class_to_json(obj):
    '''Writes the dictionary description for json serialization of an object
    '''
    return (obj.__dict__)
