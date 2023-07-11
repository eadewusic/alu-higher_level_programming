#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{a} + {b} = {result}".format(a=a, b=b, result=add(a, b)))
    print("{a} - {b} = {result}".format(a=a, b=b, result=sub(a, b)))
    print("{a} * {b} = {result}".format(a=a, b=b, result=mul(a, b)))
    print("{a} / {b} = {result}".format(a=a, b=b, result=div(a, b)))
