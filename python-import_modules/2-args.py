#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    suffix = "arguments"
    if (len(sys.argv) - 1 == 1):
        suffix = "argument"
    if (len(sys.argv) - 1 > 0):
        suffix += ":"
    else:
        suffix += "."
    print("{num} {suffix}".format(num=len(sys.argv) - 1, suffix=suffix))
    for i in range(1, len(sys.argv)):
        print("{num}: {value}".format(num=i, value=sys.argv[i]))
