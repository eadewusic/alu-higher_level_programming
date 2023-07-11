#!/usr/bin/python3

for i in range(122, 96, -1):
    if (i % 2 == 1):
        print("{letter}".format(letter=chr(i - 32)), end="")
    else:
        print("{letter}".format(letter=chr(i)), end="")
