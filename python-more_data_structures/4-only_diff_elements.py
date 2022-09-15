#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    myset = {*set_1, * set_2}
    common = [i for i in set_1 if i in set_2]
    diff = myset - set(common)
    return diff
