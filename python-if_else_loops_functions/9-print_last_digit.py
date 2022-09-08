#!/usr/bin/python3
def print_last_digit(number):
    print((abs(number) % 10), end="")
    if number < 0:
        last = abs(number) % 10
        return (last)
