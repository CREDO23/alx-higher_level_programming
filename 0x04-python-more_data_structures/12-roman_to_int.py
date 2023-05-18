#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    romans_num = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0
    i = 0

    if len(roman_string) == 1:
        return romans_num[roman_string]

    while (i < len(roman_string)):

        prev = romans_num[roman_string[i]]

        if (i < len(roman_string) - 1):
            next = romans_num[roman_string[i + 1]]

        if prev < next:
            int_num += next - prev
            i += 2
        elif prev >= next:
            int_num += prev
            i += 1

    return int_num
