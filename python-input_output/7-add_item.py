#!/usr/bin/python3
'''script adds all arguments to a python list
'''
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_list = []
json_list += sys.argv[1:]
save_to_json_file(json_list, "add_item.json")
