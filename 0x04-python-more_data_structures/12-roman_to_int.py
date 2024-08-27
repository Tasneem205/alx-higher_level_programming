#!/usr/bin/python3
"""
convert from roman to int
"""


def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    cur = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    for i in roman_string:
        value = dic.get(i, 0)
        if value > cur:
            res += value - 2 * cur
        else:
            res += value
        cur = value
    return res
