#!/usr/bin/python3
print(__import__("my_module").__doc__)
print(__import__("my_module").MyClass.__doc__)
print(__import__("my_module").my_function.__doc__)
print(__import__("my_module").MyClass.my_function.__doc__)


class Square:
    pass
