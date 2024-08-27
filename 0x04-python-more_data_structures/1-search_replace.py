#!/usr/bin/python3
"""
search and replace with new element
"""


def search_replace(my_list, search, replace):
    new_list = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
