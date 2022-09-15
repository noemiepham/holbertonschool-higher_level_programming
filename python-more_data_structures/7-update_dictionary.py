#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Method 2:
    #  newdict = {key: value}
    # a_dictionary.update(newdict)
    # return a_dictionary

    for key, value in a_dictionary.items():
        a_dictionary[key] = value
        return (a_dictionary)
