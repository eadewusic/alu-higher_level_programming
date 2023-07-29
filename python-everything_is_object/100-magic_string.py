#!/usr/bin/python3
def magic_string():
    """
    Returns a string "BestSchool" concatenated with itself n times, where n is the number of times
    the function has been called.

    Returns:
        str: A string containing "BestSchool" repeated n times separated by commas.
    """
    if not hasattr(magic_string, "count"):
        magic_string.count = 1
    else:
        magic_string.count += 1
    return "BestSchool" + (", BestSchool" * (magic_string.count - 1))
