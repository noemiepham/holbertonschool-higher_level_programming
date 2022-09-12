## Python - Data Structures: Lists, Tuples

### 1 Why Python programming is awesome

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java. 

It can be used for the programming of the front end (client side) with which users interact and back end (server side) database of your website. It can be used for numerical and data analysis for scientific study and research. It can be used to develop artificial intelligence.

It can be used to develop both online and offline applications from productivity tools, games and other type of app you can think off.

### 2 What are lists and how to use them

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```
$ thislist = ["apple", "banana", "cherry"]
$ print(thislist)
```
Lists and tuples are Python’s most used data types. The tuple data type in Python is similar to a list with one difference that element values of a tuple can not be modified, and tuple items are put between parentheses instead of a square bracket.

```
$ tuples = ("apple", "banana", "cherry")
$ list = print(list(tuples)) 
// list = ["apple", "banana", "cherry"]
```

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
2) list.count(x): is used to determine how many times a given item x appears in a list.
3) list.sort(key=None, reverse=False):

The Python list method sort() sorts list data in place. It takes in two keyword arguments.

###### key(defaults to None): It specifies a function of one argument used to extract items from the list and prepares them for comparison. For example, if we have a list of positive numbers, but we want our sort function to sort their negative values, we can use this key to achieve this.
###### reverse(defaults to False): It is a boolean value and if set to True, it will sort in descending order. Its value is False by default hence it sorts in ascending order.
#### Other Methods
1) list.copy():  method is used to make a copy of a list. This method is useful for keeping original list values before modifying the list.
2) list.reverse()

### How to use lists as stacks and queues
### What are list comprehensions and how to use them
### What are tuples and how to use them
### When to use tuples versus lists
### What is a sequence
### What is tuple packing
### What is sequence unpacking
### What is the del statement and how to use it

## Reference
- [w3schools](https://www.w3schools.com/python/ref_list_append.asp)
- [pythonbasics.org](https://pythonbasics.org/why-python-is-awesome/)
