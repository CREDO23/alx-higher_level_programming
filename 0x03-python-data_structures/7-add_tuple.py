#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new = list()

    for i in range(2):

        a = 0
        b = 0

        if (i < len(tuple_a)):
            a = tuple_a[i]

        if (i < len(tuple_b)):
            b = tuple_b[i]

        new.append(a + b)
    return tuple(new)
