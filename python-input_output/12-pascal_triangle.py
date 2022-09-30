#!/usr/bin/python3
"""pascal_triangle
"""


def pascal_triangle(n):
    """
    add two next number
    """
    if n <= 0:
        return []

    result = []
    for obj in range(n):
        if obj == 0:
            result.append([1])
            continue
        if obj == 1:
            result.append([1, 1])
            continue
        newlist = []
        # init row
        for item in range(obj + 1):
            newlist.append(item)
        for item in range(1, obj):
            newlist[0] = 1
            newlist[obj] = 1
            newlist[item] = result[obj - 1][item] + result[obj - 1][item - 1]
        result.append(newlist)

    return result
