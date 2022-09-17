#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
          count = 0
          while count < x:
            print("{}".format(my_list[count]), end="")
            count += 1
          print()
          return (count)
    except IndexError:
        print()
        return (count)
        pass

# if x == 0 or my_list == []:
#    return (0)
# else:
#    for i in my_list[:x]:
#          print("{}".format(i), end="")
#   print()
#   return (i)
