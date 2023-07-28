#!/usr/bin/python3
'''Defines function called write_file
'''


def write_file(filename="", text=""):
    '''Writes text to filename

    Args:
       filename (str): The directory to the file being modified
       text (str): The string written into filename.
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        size = f.write(text)
    return size
