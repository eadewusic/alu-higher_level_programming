#!/usr/bin/python3
"""
This module defines a function that multiplies 2 matrices
Prototype: def matrix_mul(m_a, m_b):
You are not allowed to import any module
"""


def matrix_mul(m_a, m_b):
    '''
    Multiplies two matrices together

    Args:
       m_a (list of list of integers/floats): The first matrix
       m_a (list of lists of integers/floats): The second matrix
    '''
    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    elif not (all(map(lambda x: isinstance(x, list), m_a))):
        raise TypeError("m_a must be a list of lists")
    elif ((len(m_a) == 0) or (sum(map(lambda x: len(x), m_a)) == 0)):
        raise ValueError("m_a can't be empty")
    elif not (all(map(lambda x: all(map(lambda y: isinstance(y, (float, int)), x)), m_a))):
        raise TypeError("m_a should contain only integers or floats")
    elif not (all(map(lambda x: len(m_a[0]) == len(x), m_a))):
        raise TypeError("each row of m_a must be of the same size")
    if not (isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    elif not (all(map(lambda x: isinstance(x, list), m_b))):
        raise TypeError("m_b must be a list of lists")
    elif ((len(m_b) == 0) or (sum(map(lambda x: len(x), m_b)) == 0)):
        raise ValueError("m_b can't be empty")
    elif not (all(map(lambda x: all(map(lambda y: isinstance(y, (float, int)), x)), m_b))):
        raise TypeError("m_b should contain only integers or floats")
    elif not (all(map(lambda x: len(m_b[0]) == len(x), m_b))):
        raise TypeError("each row of m_b must be of the same size")
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

        new_matrix = []
        for row in m_a:
            new_row = []
            for col in inverted_b:
                prod = 0
                for i in range(len(inverted_b[0])):
                    prod += row[i] * col[i]
                new_row.append(prod)
            new_matrix.append(new_row)

        return new_matrix
