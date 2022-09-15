#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    total = sum(uniq)
    return total

    # method 2
    #    sum = 0
    #    uniq = set(my_list)
    #    for num in uniq:
    #       sum += num
    #    return sum
