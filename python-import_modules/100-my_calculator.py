#!/usr/bin/python3

import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if operator == "+":
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} {operator} {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} {operator} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
