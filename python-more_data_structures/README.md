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

6 Methods to iterate through set in Python:

1. Using for loop statement

```
my_set = {'london', 'new york', 'seattle', 'sydney','chicago'}
for item in my_set:
  print(item)
  
```

 2. Enumerating (Liet ke) over a set
 
```  
my_set = {'london', 'new york', 'seattle', 'sydney','chicago'}
for counter, item in enumerate(my_set):
  print(item) 
  
```
3. Using iter with for loop

We can use the iter() method as well for iterating through a python set. The iter() method will return an iterator. Using that iterator, we can iterate over a given object. We shall use the iter() method with a for loop.

```
my_set = {'london', 'new york', 'seattle', 'sydney','chicago'}
for item in iter(my_set):
  print(item)
  // london
seattle
new york
chicago
sydney

```

 4 Converting the set to a list
 
```
 for i in range(0,len(my_list)):
  print(my_list[i])
```

5. Using comprehension

``` 
Syntax: [expression for item in list]

my_set = {'london', 'new york', 'seattle', 'sydney','chicago'}
val = [print(item) for item in my_set]
```

6. Iterating over two sets simultaneously using zip()

``` 
set1 = {10, 20, 30, 40, 50}

set2 = {100, 200, 300, 400, 500}

Using the zip() function, we shall create two iterables for each set – ‘i1’ and ‘i2’. Then, we shall print i1 and i2.

for (i1, i2) in zip(set1, set2): 
    print(i1, i2) 
// output: 
40 100
10 200
50 300
20 400
30 500
```

## What are dictionaries and how to use them

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values:

```
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
//output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

```

## When to use dictionaries versus lists or sets

Use dictionaries for the lookup of elements as it is faster than a list and takes less time to traverse.

## What is a key in a dictionary

Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

## How to iterate over a dictionary

- Iterating Through Keys Directly
- Iterating Through .items()
- Iterating Through .keys()
- Iterating Through .values()

## What is a lambda function

- A lambda function can take any number of arguments, but they contain only a single expression. An expression is a piece of code executed by the lambda function, which may or may not return any value.
- Lambda functions can be used to return function objects.
- Syntactically, lambda functions are restricted to only a single expression.

```
lambda argument(s): expression
``` 
``` 
product = lambda x, y : x * y

print(product(2, 3))
//6
```
## What are the map, reduce and filter functions 

The map() function is a higher-order function. As previously stated, this function accepts another function and a sequence of ‘iterables’ as parameters and provides output after applying the function to each iterable in the sequence.

``` 
SYNTAX: map(function, iterables)

````
````
tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup)) 
print(newtuple)
// (8, 10, 25, 100, 57, 65, 80, 26, 76, 64)
``` 
The filter() function is used to generate an output list of values that return true when the function is called. It has the following syntax:

````
SYNTAX: filter (function, iterables)
````


map(), can take user-defined functions and lambda functions as parameters.



y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))
// [3, 4]



reduce() function applies a provided function to ‘iterables’ and returns a single value, as the name implies


SYNTAX: reduce(function, iterables)

Example: 


from functools import reduce
reduce(lambda a,b: a+b,[23,21,45,98])
OUTPUT
187

## Reference

[w3schools](https://www.w3schools.com/python/ref_list_append.asp)
[pythonbasics.org](https://pythonbasics.org/why-python-is-awesome/)
[realpython.com](https://realpython.com/list-comprehension-python/)
[javatpoint.com/](https://www.javatpoint.com/python-del-statement)
