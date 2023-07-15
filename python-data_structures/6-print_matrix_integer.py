#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return 1
    for m_rows in matrix:
        for j, n_columns in enumerate(m_rows):
            if j < len(m_rows) - 1:
                print("{:d} ".format(n_columns), end="")
            else:
                print("{:d}".format(n_columns), end="")
        print()
    return 0
