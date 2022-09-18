#!/usr/bin/python3
import sys


def safe_function(fct, *args):
     try:
          for argv in range(len(args)):
               id(fct(args[0], args[1]))
     except (ZeroDivisionError, IndexError, TypeError) as error:
          print("Exception:{}".format(error), file=sys.stderr)
          return