#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    sz = len(list_of_integers)
    md_e = sz
    md = sz // 2

    if sz == 0:
        return None

    while True:
        md_e = md_e // 2
        if (md < sz - 1 and
                list_of_integers[md] < list_of_integers[md + 1]):
            if md_e // 2 == 0:
                md_e = 2
            md = md + md_e // 2
        elif md_e > 0 and list_of_integers[md] < list_of_integers[md - 1]:
            if md_e // 2 == 0:
                md_e = 2
            md = md - md_e // 2
        else:
            return list_of_integers[md]