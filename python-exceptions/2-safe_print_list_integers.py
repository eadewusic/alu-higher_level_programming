#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        i = 0
        while True:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed += 1
                if printed == x:
                    break
            i += 1
    except IndexError:
        pass
    finally:
        print()
        return printed
