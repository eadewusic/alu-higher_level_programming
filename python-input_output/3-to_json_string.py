#!/usr/bin/python3
'''Defines function to_json_string
'''
import json


def to_json_string(my_obj):
    '''Returns the json representation of a string object
    '''
    return (json.dumps(my_obj))
