#!/usr/bin/python3
"""
defining a class Mylist
"""


class MyList(list):
    """
    class mylist
    """
    def print_sorted(self):
        """
        print sorted list
        """
        a = sorted(self)
        print(a)
