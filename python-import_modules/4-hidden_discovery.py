#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    sorted_names = sorted(names)
    for name in sorted_names:
        if (name[0:2] != "__"):
            print(name)
