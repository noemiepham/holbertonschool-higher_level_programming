#!/usr/bin/python3
def remove_char_at(str, n):
    lenStr = len(str)
    if lenStr <= n or n < 0:
        return str
    else:
        for i in range(lenStr):
            return str[:n-1] + str[n:]
