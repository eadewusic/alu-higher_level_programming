#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, 'count', 0) + 1
    return 'BestSchool' + (', BestSchool' * (magic_string.count - 1))
