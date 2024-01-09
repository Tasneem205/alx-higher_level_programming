#!/usr/bin/python3

def no_c(my_string):
    n = len(my_string)
    s = ""

    for i in range(n):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            s += my_string[i]

    return s
