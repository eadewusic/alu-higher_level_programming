#!/usr/bin/python3

from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{a} + {b} = {result}".format(a=a, b=b, result=add(a, b)))
