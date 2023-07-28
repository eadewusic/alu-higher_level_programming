#!/usr/bin/python3
"""
defining a class MyList
"""


class MyList(list):
    """
    Class MyList, inheriting from the built-in list class.

    Public instance method:
    - print_sorted(): Prints the list in ascending order (sorted).
    """
    def print_sorted(self):
        """
        Print the list in ascending order (sorted).
        """
        sorted_list = sorted(self)
        print(sorted_list)
