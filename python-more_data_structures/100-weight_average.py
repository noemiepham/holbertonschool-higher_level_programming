#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0.0
    Values = list((t[0] * t[1] for t in my_list))
    Weights = list(t[1] for t in my_list)
    result = sum(Values) / sum(Weights)
    return (result)
