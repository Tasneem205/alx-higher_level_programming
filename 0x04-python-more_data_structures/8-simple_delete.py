#!/usr/bin/python3
"""
update a dict with new key or replace val
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
