#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None
    
    best_key = ''
    best_score = float('-inf')

    for k in a_dictionary:
        if a_dictionary[k] > best_score:
            best_score = a_dictionary[k]
            best_key = k

    return best_key
