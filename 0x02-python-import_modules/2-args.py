#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':

    lenarg = len(argv) - 1

    print("{} ".format(lenarg), end="")

    print("argument{}".format(('s', '')[lenarg == 1]), end="")

    print("{}".format((':', '.')[lenarg == 0]))

    for i in range(1, lenarg + 1):
        print("{}: {}".format(i, argv[i]))
