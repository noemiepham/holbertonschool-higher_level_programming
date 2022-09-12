## Python - Data Structures: Lists, Tuples

### 1 Why Python programming is awesome

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java. 

It can be used for the programming of the front end (client side) with which users interact and back end (server side) database of your website. It can be used for numerical and data analysis for scientific study and research. It can be used to develop artificial intelligence.

It can be used to develop both online and offline applications from productivity tools, games and other type of app you can think off.

### 2 What are lists and how to use them

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
        - List is a collection which is ordered and changeable. Allows duplicate members.
        - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
        - Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
        - Dictionary is a collection which is ordered** and changeable. No duplicate members.

Lists are created using square brackets:

```
$ thislist = ["apple", "banana", "cherry"]
$ print(thislist)
```
Lists and tuples are Python’s most used data types. 

### 3 What are the differences and similarities between strings and lists

The similarity between Lists and Strings in Python is that both are sequences. 

The differences between them are that:
- Firstly, Lists are mutable but Strings are immutable. List and array in Python 
- Secondly, elements of a list can be of different types whereas a String only contains characters that are all of String type. List and array in Python can either be homogeneous or heterogeneous
```
>> Homogenous Lists:
$  list = ["apple", "banana", "cherry"]
$  list = [1, 2, 3, 4]
>> Heterogeneous Lists:
$  list = [1, "apple", 2.2,  "banana", "cherry"]
```

### 4 What are the most common methods of lists and how to use them
#### Method For Addition
1) list.append(x): method is used to insert a new item at the end of the list
```
list.append (item)
```
2) list.extend(iterable): method is used to merge two list items and store the merged items in the first list.
```
first_list.extend(second_list)
```

3) list.insert(i,x): method is used to insert a new item into a particular position in the list
```
list.insert(position, item)
```

#### Method For Subtraction
1) list.pop( [i] ): remove items from this list at any index position we wish to, thanks to pop()
```
>>> cars = ['Toyota','Audi','BMW','Bugatti','Bently','Aston Martin']
>>> toyota = cars.pop(0) # remove and return car at index 0
>>> cars
['Audi', 'BMW', 'Bugatti', 'Bently', 'Aston Martin']
```


2) list.remove(x): removes the first occurrence of an item that is equal to x
```
>>> listdata = ['Mango', 'Banana', 'Orange', 'grape', 'Guava', 'Watermelon']
>>> listdata.remove('Banana')
['Mango', 'Orange', 'grape', 'Guava', 'Watermelon']
```
3) list.clear() : removes all items from the list, thereby making it empty. It takes no arguments.
```
names = ['enow','kevin','eyong']   # our collection of names
>>> names.clear()                              # clear the list object
>>> names
[]
```
#### Methods For Analyzing
1) list.index[x[,start[,end]]) : search item value as the input and returns with the position value of the item in the list, if it exists; otherwise, it generates a ValueError. 

```
my_string = "Hello World!"
my_string.index("l") # outputs 2
```
2) list.count(x): is used to determine how many times a given item x appears in a list.
```
Format: string.count(sub, start= 0,end=len(string))
string =  "Add Grepper Answer"
print(string.count('e')
>>> 
```
 
5) list.sort(key=None, reverse=False):
```
>>> x = [1 ,11, 2, 3]
>>> y = sorted(x)
>>> x
[1, 11, 2, 3]
>>> y
[1, 2, 3, 11]
```
The Python list method sort() sorts list data in place. It takes in two keyword arguments.

###### key(defaults to None): It specifies a function of one argument used to extract items from the list and prepares them for comparison. For example, if we have a list of positive numbers, but we want our sort function to sort their negative values, we can use this key to achieve this.
###### reverse(defaults to False): It is a boolean value and if set to True, it will sort in descending order. Its value is False by default hence it sorts in ascending order.
#### Other Methods
1) list.copy():  method is used to make a copy of a list. This method is useful for keeping original list values before modifying the list.
```
spring_fruits = ['Apricot', 'Avocado', 'Kiwi', 'Grapefruit', 'Cherry', 'Strawberry']

summer_fruits = list(spring_fruits)

print(summer_fruits)
Our code returns the following new list:

['Apricot', 'Avocado', 'Kiwi', 'Grapefruit', 'Cherry', 'Strawberry']
``` 

3) list.reverse()
```
the_list = [1,2,3]
reversed_list = the_list.reverse()
list(reversed_list) # will return [3,2,1]

# OR, better

the_list = [1,2,3]
the_list[::-1] # will also return [3,2,1]
``` 


### How to use lists as stacks and queues
##### Stack:  

Stack works on the principle of “Last-in, first-out” (LIFO).

To add an item to the top of the list, i.e., to push an item, we use append() function and to pop out an element we use pop() function
```
>>> spring_fruits = ['Apricot', 'Avocado', 'Kiwi', 'Grapefruit', 'Cherry']
>>> spring_fruits.append('Strawberry')
>>> print(spring_fruits)
['Apricot', 'Avocado', 'Kiwi', 'Grapefruit', 'Cherry','Strawberry' ]
>>> spring_fruits.pop()
>>> print(spring_fruits)
['Apricot', 'Avocado', 'Kiwi', 'Grapefruit', 'Cherry']
``` 
###### Queue
Works on the principle of “First-in, first-out”.(FIFO)

Below is list implementation of queue. We use pop(0) to remove the first item from a list
```
from collections import deque
queue=deque([1,2,3])
#adds elements to the end of list
queue.append(4)
print (queue)#Output:deque([1, 2, 3, 4])
queue.append(5)
print (queue)#Output:deque([1, 2, 3, 4, 5])


#retrieves element from begining of list. (first in  first out.)
print (queue.popleft())#Output:1
print (queue)#Output:deque([2, 3, 4, 5])
``` 


### What are list comprehensions and how to use them
- Python list comprehensions allow you to create a new list from an existing one. List comprehension offers a shorter syntax .
- Use list comprehensions instead of map(), for loop or filter() to make your code more concise and readable.

```
The Syntax:

newlist = [expression for item in iterable if condition == True]
```  
Creat new list with For Loop
```  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
['apple', 'banana', 'mango']
```  
Creat new list comprehensions
```  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
['apple', 'banana', 'mango']
```  


### What are tuples and how to use them

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

```
$ tuples = ("apple", "banana", "cherry")
$ list = print(list(tuples)) 
// list = ["apple", "banana", "cherry"]
```
- We can use tuples to swap the values associated with variables only if the variables are tuple elements. 
```  
x = 19
y = 91
print('Before swapping:')
print(f'x = {x}, y = {y}')
(x, y) = (y, x)
print('After swapping:')
print(f'x = {x}, y = {y}')
```
- Returning More Than One Value from a Function
```  
def sum_and_avg(x, y, z):
    s = x + y + z
    a = s/3
    return(s, a)
(S, A) = sum_and_avg(3, 8, 5)
print('Sum =', S)
print('Avg =', A)
Sum = 16
Avg = 5.333333333333333
```  

### When to use tuples versus lists
### What is a sequence

A sequence is a positionally ordered collection of items. And you can refer to any item in the sequence by using its index number e.g., s[0] and s[1].

In Python, the sequence index starts at 0, not 1. So the first element is s[0] and the second element is s[1]. If the sequence s has n items, the last item is s[n-1].

Python has the following built-in sequence types: lists, bytearrays, strings, tuples, range, and bytes. Python classifies sequence types as mutable and immutable.

### What is tuple packing

In packing, we place value into a new tuple while in unpacking we extract those values back into variables.

```  
#!/usr/bin/python3
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(x) // ("Guru99", 20, "Education") 
print(company) // Guru99
print(emp) // 20
print(profile) // Education

```
###### Unpacking Tuples
Unpacking a tuple allows us to extract the tuple elements and assign them to named variables. Let’s try it:
``` 
first_name, last_name, age = customers[2]
print(first_name, last_name, ',', age, 'years old')
Mehdi Lotfinejad , 39 years old
``` 

### What is sequence unpacking

Sequence unpacking in python allows you to take objects in a collection and store them in variables for later use. This is particularly useful when a function or method returns a sequence of objects.
```  
>>> new_run = ['09/01/2020', '10:00', 60, 6, 100]

We can unpack this list with appropriately named variables by assignment:

>>> date, pace, time, distance, elevation = new_run 

We can then print the values for these variables to validate that the assignments were correct:

$ print("Date: ", date)
$ print("Pace: ", pace, 'min')
$ print("Time: ", time, 'min')
$ print("Distance: ", distance, 'miles')
$ print("Elevation: ", elevation, 'feet')

Date: 09/01/2022
Pade: 10:00 min
....
```  
### What is the del statement and how to use it

In Python, the del keyword is generally used to delete an object. 

Since everything in Python represents some kind of object, the del keyword can also be used to delete lists, variables, parts of a list, etc.

The del statement does not return any type of value.

``` 
a = 13  
b = 5  
c = a + b + 13 - 1 + 5  
print(c)   // 35
  
# delete the c variables  
del c  
  
# print c variable after delete  
print(c)  // NameError: name 'c' is not defined
``` 

## Reference
- [w3schools](https://www.w3schools.com/python/ref_list_append.asp)
- [pythonbasics.org](https://pythonbasics.org/why-python-is-awesome/)
- [realpython.com](https://realpython.com/list-comprehension-python/)
- [javatpoint.com/](https://www.javatpoint.com/python-del-statement)
