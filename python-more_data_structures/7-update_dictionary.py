#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newdict = {key: value}
    a_dictionary.update(newdict)
    return a_dictionary

    # Method 2: for key, value in a_dictionary.items():
    #     a_dictionary[key] = value
    # return (a_dictionary)
