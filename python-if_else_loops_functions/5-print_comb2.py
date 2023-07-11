#!/usr/bin/python3

for i in range(100):
    if (i != 99):
        print("{num:02}".format(num=i), end=", ")
    else:
        print("{num:02}".format(num=i), end="\n")
