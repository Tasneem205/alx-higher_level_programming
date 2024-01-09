#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    i = len(my_list)
    newList = [0]*i

    for x in range(i):
        newList[x] = my_list[x]

    if (idx < 0 or idx >= i):
        return newList

    newList[idx] = element
    return newList
