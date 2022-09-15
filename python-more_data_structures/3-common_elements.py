#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 & set_2:
        common = set_1 & set_2

    # method 2
    # common = i for i in set_1 if i in set_b
    # return common
