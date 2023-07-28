#!/usr/bin/python3
'''Defines afunction called load_from_json_file
'''
import json


def load_from_json_file(filename):
    '''Creates an object from a json file

    Args:
       filename  (str): File object is derived from
    '''
    with open(filename, 'r') as f:
        my_obj = json.load(f)
    return my_obj
