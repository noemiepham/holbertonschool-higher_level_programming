#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    numArgv = len(sys.argv)
    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])
    if numArgv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit("1")
    else:
        if sign == '+':
            calcul = add(a, b)
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif sign == '-':
            calcul = sub(a, b)
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif sign == "*":
            calcul = mul(a, b)
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif sign == '/':
            calcul = div(a, b)
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit("1")
