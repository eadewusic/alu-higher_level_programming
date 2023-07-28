#!/usr/bin/python3
'''Defines a function called read_file
'''


def read_file(filename=""):
    '''Reads a file and prints it out

    Args:
       filename (dir): The path to the file being read

    Return: none
    '''
    with open(filename) as f:
        for line in f:
            print(line, end="")
