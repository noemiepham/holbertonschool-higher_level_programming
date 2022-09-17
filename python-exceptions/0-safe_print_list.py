#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(int(x)):
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
        return (i)
    except IndexError:
        print()
        return (i)
        pass

# if x == 0 or my_list == []:
#    return (0)
# else:
#    for i in my_list[:x]:
#          print("{}".format(i), end="")
#   print()
#   return (i)
