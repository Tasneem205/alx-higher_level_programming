#!/usr/bin/python3
"""
add all unique items to a list
"""


def uniq_add(my_list=[]):
    new_list = []
    res = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            res += i
    return res
