#!/usr/bin/python3
'''Defines function append_after
'''


def append_after(filename="", search_string="", new_string=""):
    ''' a function that inserts a line of text to a file,
    after each line containing a specific string.
    '''
    s = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            s += line
            if search_string in line:
                s += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(s)
