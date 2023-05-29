#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nb_el = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            nb_el += 1

        nb_el

        print("")
        return nb_el
    except Exception:
        print("")
        return nb_el
