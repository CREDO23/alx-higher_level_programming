#!/usr/bin/python3

from sys import argv

if __name__ == '__main__':

    lenarg = len(argv) - 1
    result = 0

    for i in range(1, lenarg + 1):
        result += int(argv[i])

    print("{}".format(result))
