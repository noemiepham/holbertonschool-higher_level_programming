#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").__doc__)'''


def add_integer(a, b=98):
     try:
          return (int(a) + int(b))
     except:
          if type(a) != int:
               raise TypeError('a must be an integer')
          if type(b) != int:
               raise TypeError('b must be an interger')

if __name__ == "__main__":
    import doctest
    doctest.testmod()