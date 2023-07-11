#!/usr/bin/python3

for i in range(9):
    for j in range(i + 1, 10):
        if (i == 8 and j == 9):
            print("{num:02}".format(num=((i * 10) + j)), end="\n")
        else:
            print("{num:02}".format(num=((i * 10) + j)), end=", ")
