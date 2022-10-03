#!/usr/bin/python3
"""import module"""
import sys
import io
dic_status = {}
size = 0
count = 0
for line in sys.stdin:
    split = line.split()
    status = split[-2]
    size += int(split[-1])
    if status in dic_status.keys():
        dic_status[status] += 1
    else:
        dic_status[status] = 1
    count += 1
    if count == 10:
        sort = sorted(dic_status.keys())
        print("File size:", size)
        for keys in sort:
            print("{}: {}".format(keys, dic_status[keys]))
        count = 0
        continue
