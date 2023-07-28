#!/usr/bin/python3
'''Defines function from_json_string
'''
import json


def from_json_string(my_str):
    '''Function converts json string to a python object
    '''
    return (json.loads(my_str))
