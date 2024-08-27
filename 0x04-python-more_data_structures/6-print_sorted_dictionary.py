#!/usr/bin/python3
"""
sort the dict by keys
"""


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")

