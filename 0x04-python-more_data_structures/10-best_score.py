#!/usr/bin/python3
"""
multiply every value by two
"""


def best_score(a_dictionary):
    score = 0
    ans = None
    if a_dictionary is None:
        return None
    for k in a_dictionary:
        if a_dictionary[k] > score:
            score = a_dictionary[k]
            ans = k
    return ans
