#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return 1
    lengthOfList = len(my_list)
    while lengthOfList >= 1:
        print("{:d}".format(my_list[lengthOfList - 1]))
        lengthOfList -= 1
    return 0
