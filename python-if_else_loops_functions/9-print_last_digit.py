#!/usr/bin/python3


def print_last_digit(number):
    unsigned_num = abs(number)
    last_digit = unsigned_num % 10
    print(f"{last_digit}", end="")
    return (last_digit)
