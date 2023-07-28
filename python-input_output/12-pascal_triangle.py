#!/usr/bin/python3
'''Creates a function pascal_triangle
'''


def pascal_triangle(n):
    '''Function returns a list of lists of integers
    representing a pascals triangle
    '''
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
            continue
        else:
            new_entry = [1]
            for j in range(1, i):
                new_entry.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            new_entry.append(1)
            triangle.append(new_entry)
    return triangle
