#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    best_key = list(a_dictionary)[0]

    for k in a_dictionary:
        if a_dictionary[k] > a_dictionary[best_key]:
            best_key = k

    return best_key
