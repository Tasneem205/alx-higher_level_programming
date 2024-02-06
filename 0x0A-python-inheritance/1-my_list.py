#!/usr/bin/python3
'''Module for my list'''


class MyList(list):
    '''custom class MyList class'''
    def print_sorted(self):
        '''print sorted list'''
        print(sorted(self))
