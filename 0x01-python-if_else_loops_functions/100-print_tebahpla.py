#!/usr/bin/python3

for i in reversed(range(97, 123)):
    ch = ''

    if (i % 2):
        ch = chr(i - 32)
    else:
        ch = chr(i)
    print("{}".format(ch), end="")
