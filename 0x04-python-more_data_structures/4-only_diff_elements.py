#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()

    for el in set_1:
        if el not in set_2:
            new_set.add(el)
    for el in set_2:
        if el not in set_1:
            new_set.add(el)

    return new_set
