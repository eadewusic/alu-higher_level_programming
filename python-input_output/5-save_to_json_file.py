#!/usr/bin/python3
'''Defines function save_to_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes an object to a json file

    Args:
       my_obj (object): The object being written
       filename (str): The name of the file to be saved to
    '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
