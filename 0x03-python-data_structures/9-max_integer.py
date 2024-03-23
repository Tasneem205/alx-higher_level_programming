#!/usr/bin/python3


def max_integer(my_list=[]):
    max = float('-inf')
    if len(my_list) >= 1:
        for i in my_list:
            if i > max:
                max = i
        return max
    return None
