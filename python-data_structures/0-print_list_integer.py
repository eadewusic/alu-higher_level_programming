#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for num in my_list:
        try:
            print("{:d}".format(num))
        except ValueError:
            print("Invalid integer:", num)


# Test case 1
my_list = [1]
print_list_integer(my_list)

# Test case 2
my_list = []
print_list_integer(my_list)

# Test case 3
my_list = [1, 2, "H", 9]
print_list_integer(my_list)
