#!/usr/bin/python3
'''Defines function append_write
'''


def append_write(filename="", text=""):
    '''Appends text to the end of the file specified by filename
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        size = f.write(text)
    return size
