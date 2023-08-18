#!/usr/bin/python3
""" 1-main module"""
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

    r4 = Rectangle(1, 2)
    print(r4.id)

    r5 = Rectangle(1, 2, 3)
    print(r5.id)

    r6 = Rectangle(1, 2, 3, 4)
    print(r6.id)

    r7 = Rectangle("1", 2)
    print(r7.width)
    print(r7.id)

    r7 = Rectangle(1, "2")
    print(r7.x)
    print(r7.y)
    print(r7.id)

    r7 = Rectangle(1, 2, "3")
    print(r7.y)
    print(r7.id)

    r7 = Rectangle(1, 2, 3, "4")
    # r7.y = -10
    print(r7.y)
    print(r7.id)
