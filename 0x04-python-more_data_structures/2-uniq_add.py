#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for s in set(my_list):
        add += s
    return add
