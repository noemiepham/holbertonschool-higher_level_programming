#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv)
if i < 2:
    print("0 arguments.")
elif i == 2:
    print("1: argument:")
    print("{}: {}".format(j, sys.argv[j]))

else:
    print("{} arguments:".format(i - 1))
for j in range(1, i):
    print("{}: {}".format(j, sys.argv[j]))
