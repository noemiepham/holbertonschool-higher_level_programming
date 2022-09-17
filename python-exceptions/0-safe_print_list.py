#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0 or my_list == []:
        return (0)
    else:
        for i in my_list[:x]:
            try:
                print("{}".format(i), end="")
            except TypeError:
                print(my_list)
            except UnboundLocalError:
                print(0)
        print()
        return (i)
