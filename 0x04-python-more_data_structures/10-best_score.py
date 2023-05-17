#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    best_key = list(a_dictionary)[0]
    best_score = a_dictionary[best_key]
    for k, v in a_dictionary.items():
        if v > best_score:
            best_score = v
            best_key = k
    return (best_key)
