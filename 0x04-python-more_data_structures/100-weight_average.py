#!/usr/bin/python3

def weight_average(my_list=[]):

    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    score = 0
    weight_sum = 0

    for i in my_list:
        score += i[0] * i[1]
        weight_sum += i[1]

    return score / weight_sum
