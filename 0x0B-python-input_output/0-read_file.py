#!/usr/bin/python3
'''This module contains a function\
      that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''Reads a text file and print it to stdout'''

    with open(filename, encoding='UTF8') as f:
        file = f.read()
        print(file, end='')
