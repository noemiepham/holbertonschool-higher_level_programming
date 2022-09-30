#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

list = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
result = weight_average(list)
print("Av: {:0.2f}".format(result))