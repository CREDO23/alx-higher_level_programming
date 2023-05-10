#!/usr/bin/python3

def uppercase(str):
    str = str + '\n'
    for i in range(0, len(str)):
        ch = ''
        if (97 <= ord(str[i]) <= 122):
            ch = chr(ord(str[i]) - 32)
        else:
            ch = str[i]
        print("{}".format(ch), end="")
