# Python - More Data Structures: Set, Dictionary

## Why Python programming is awesome

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java. 

It can be used for the programming of the front end (client side) with which users interact and back end (server side) database of your website. It can be used for numerical and data analysis for scientific study and research. It can be used to develop artificial intelligence.

It can be used to develop both online and offline applications from productivity tools, games and other type of app you can think off.

## What are sets and how to use them

Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
``` 
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1) // {"apple", "banana", "cherry"}
print(set2) // {1, 5, 7, 9, 3}
print(set3 // {1, 5, 7, 9, 3}
```

## What are the most common methods of set and how to use them
##### Add set Items
update() : To add items from another set into the current set,
##### Remove Set Items

discard(x): method removes x from the set, but doesn't raise any error if x is not present in the set.

pop(): method removes and returns a random element from the set.

clear(): method removes all elements from a set

remove(x):  function removes the element x from a set. It returns a KeyError if x is not part of the set
```
>>> sub_set.remove("guitar")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'guitar'
```

## When to use sets versus lists
## How to iterate into a set

6 Methods to iterate through set in Python

## What are dictionaries and how to use them
## When to use dictionaries versus lists or sets
## What is a key in a dictionary
## How to iterate over a dictionary
## What is a lambda function
## What are the map, reduce and filter functions 
