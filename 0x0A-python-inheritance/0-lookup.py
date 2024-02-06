#!/usr/bin/python3
'''Modeule for lockup method'''


def lookup(obj):
    '''looks up an object attributes and methods.
    Args:
    obj: the object

    Returns:
    list: the list of the attributes
    '''
    return dir(obj)
