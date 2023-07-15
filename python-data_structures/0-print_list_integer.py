#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

def print_list_integer(my_list=[]):
    for num in my_list:
        print("{}".format(num))
