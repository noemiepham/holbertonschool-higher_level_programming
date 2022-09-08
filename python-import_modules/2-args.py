#!/usr/bin/python3
import sys
if __name__ == "__main__":
i = len(sys.argv)
if i < 2:
    print("0 arguments.")
else:
    print("{} argument:".format(i - 1))
for j in range(1, i):
    print("{}: {}".format(j, sys.argv[j]))
