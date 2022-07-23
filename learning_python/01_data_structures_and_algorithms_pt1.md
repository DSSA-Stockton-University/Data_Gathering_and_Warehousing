# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2022
**Module**: 1
**Week**: 2

---
## Data Structures and Algorithms: Part I

![img](/assets/img/ds_meme.jpg)
---
**Data Structures** organizes how data is stored in memory when a computer program processes it. More simply, data structures focus on the **storage and retrieval** of information. 

**Algorithms** provide a set of instructions to process data for a specific purpose. Algorithms use data structures in a logical way to solve specific computing problems.

There are usually more than one data structure that can be used for a given task. It's not always obvious which choice is best among multiple possibilities, so its important to focus on how your program will be used. 


**Problem:** Yelp hires you to figure out the best way to store information about restaurants for their website.

**Think about how a program will be used:** Yelp helps millions of users look for restaurants by name. If you think about the usage pattern, probably 99% of users come to Yelp to find a restaurant, and somewhere less than 1% come to Yelp to set up a new restaurant. So a very, very small amount of traffic in the setup case.

**Designing the right Solution**: Given that the predominant use case is to *search* (vs Add a new Restaurant), you would probably pick a data structure that was optimized for looking up by value as opposed to inserting them into the dataset.

### Data Structures in Python

![img](/assets/img/data_structures.png)

---

#### Built-in Data Structures in Python
##### Array, List, and Tuple

An **Array** is a container which can hold a fixed number of items and these items <u>should be of the same type</u>. Most of the data structures make use of arrays to implement their algorithms.

There are two common types of arrays:
- **Static Array** - Array containing a fixed size and same data types. 
- **Dynamic Array** - is the native array type used in python, referred to as a `list`. Dynamic array's can contains a variable size and sometimes allows mixed data types. 

A **List** is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that *items in a list do not need to be of the same type.* In other words, we can have list that contain any combination of integers, floats, strings, and objects

A **tuple** is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use <u>parentheses</u>, whereas lists use square brackets.

The following are the important terms to understand the concept of Arrays:
> **Element** − Each item stored in an array is called an element.
> **Index** − Each location of an element in an array has a numerical index, which is used to identify the element.
> **Size** - Total count of elements in an Array, sometimes called length. 
> ##### Array Representation:
> ![img](/assets/img/array_representation.jpg)
> As per the above illustration, following are the important points to be considered:
> - Index starts with 0.
> - Array length is 10, which means it can store 10 elements.
> - Each element can be accessed via its index. For example, we can fetch an element at index 6 as 9.
>

Basic Operations we can make with arrays:
> 1. **Traverse** − print all the array elements one by one.
> 2. **Insertion** − Adds an element at the given index.
> 3. **Deletion** − Deletes an element at the given index.
> 4. **Search** − Searches an element using the given index or by the value.
> 5. **Update** − Updates an element at the given index.

**Note:** 
Unlike a `list` (which is a python built-in), the Array is created in Python by importing `array` module to the python program. The below code shows how both the array and list are declared:
```python
from array import *

arrayName = array(typecode, [Initializers])
# the Typecode parameter of the array specifies the data type and amount of memory allocated to each element
# the Initalizers parameter accepts a list of values denoted by square brackets "[]"

# Use comma separated values for each element in a list
listName = list(elements)
# or we can simply use square brackets
someList = ["A", 3 , 32.45, dict(best_movie='Star Wars')]

# using comma separated values to create a tuple
tupleName = ("Hello", "World", 20, 21.00)

```
|  TypeCode | Value |
|---|---|
|b| Represents signed integer of size 1 byte|
|B|Represents unsigned integer of size 1 byte|
|c|Represents character of size 1 byte
|i|Represents signed integer of size 2 bytes
|I|Represents unsigned integer of size 2 bytes
|f|Represents floating point of size 4 bytes
|d|Represents floating point of size 8 bytes   |   |
The `byte` is the unit of digital information that most commonly consists of eight bits.

The `bit` is the most basic unit of information in computing and digital communications. The bit represents a logical state with one of two possible values. These values are most commonly represented as either "1" or "0"

**Examples to try: Take 1 to 2 Minutes:**
The below examples cover how to create, access, insert, delete, update and search elements of an array, list, and tuple

**Traverse Elements**
```python
from array import *

some_array = array('i', [10,20,30,40,50])
some_list = [10,20,30,40,50]
some_tuple = (10,20,30,40,50)

# This is how to traverse an array
for x in some_array:
    print("Element in an array: ", x)

for x in some_list:
    print("Element in a list: ", x)

for x in some_tuple:
    print("Element in a tuple: ", x)
```
**Accessing Elements**
We can access each element of an array using the index of the element. The below code shows how to access an array element.
```python
# Accessing elements of an array/list using indices
from array import *

array1 = array('i', [10,20,30,40,50])
list1 = [10,20,30,40,50]
tuple1 = (10,20,30,40,50)

print("Element in an array: ", array1[0])
print("Element in an array: ", array1[2])

print("Element in a list: ", list1[0])
print("Element in a list: ", list1[2])

print("Element in a tuple: ", tuple1[0])
print("Element in a tuple: ", tuple1[2])
```
**Insertion Operation**
Insert operation is used to insert one or more data elements into an array. Insertion allows a new element to be added at the beginning, end, or any given index of array.

```python
from array import *

array1 = array('i', [10,20,30,40,50])
list1 = [10,20,30,40,50]
tuple1 = (10,20,30,40,50) # You cannot insert new values to a tuple

# insert(index, object) is a python built-in with two parameters index, and object
# index refers to the location in the array
# object refers to the value(s) to be inserted
array1.insert(1,60) # at index 1 insert value of 60
list1.insert(1, 60) # at index 1 insert value of 60

# append(object) inserts elements to the end of an array
array1.append(32)
list1.append(3) # for fun change 3 to a string data type "car"

# extend(list) inserts all elements of one array to the end of another
# if extending an array with a list make sure all elements are the same datatype
array1.extend(list1)

# now we can traverse both arrays for the results
for x in array1:
    print('from array', x)

for x in list1:
    print('from list', x)

```

**Deletion Operation**
Deletion refers to removing an existing element from the array and re-organizing all elements of an array.

```python
from array import *

array1 = array('i', [10,20,30,40,50])
list1 = [10,20,30,40,50]
tuple1 = (10,20,30,40,50) #you cannot delete elements in a tuple

# remove(value) is a python built in that uses the element value 
# remove() will remove the first matching value, not a specific index:
array1.remove(40)
list1.remove(40)

# del removes the item at a specific index:
del array1[0]
del list1[0]
del tuple1 # you can delete the whole tuple though. 

# pop(index) removes the item at a specific index and returns it.
array1.pop(-1) # -1 gives us the last element in the array
list1.pop(-1) # -1 gives us the last element in the array

for x in array1:
   print(x, 'remains from the array')

for x in list1:
   print(x, ' remains from the list')
```
**Search Operation**
You can perform a search for an array's element based on its value or its index.
```python
from array import *

array1 = array('i', [10,20,30,40,50])
list1 = [10,20,30,40,50]
tuple1 = (10,20,30,40,50)

# print the index for element value 40
print(array1.index(40))
print(list1.index(40))
print(tuple1.index(40))

# print the value of elements from the searching by index
print(array1[2:])
print(list1[2:])
print(tuple1[2:])
```
**Update Operation**
Update operation refers to updating an existing element from the array at a given index.
```python
from array import *

array1 = array('i', [10,20,30,40,50])
list1 = [10,20,30,40,50]
tuple1 = (10,20,30,40,50) # you cannot update elements in a tuple

# at an index of 2, update the value to 80
array1[2] = 80
list1[2] = 80
tuple2 = tuple1[:2] + ("new", "tuple", "elements") # you can create a new tuple to replace discarded elements from the original tuple

for x in array1:
    print(x)

for x in list1:
    print(x)

for x in tuple2:
    print(x)
```

|List   | Array   | Tuple |
|---|---|---|
| List is mutable |	Array is mutable  |  Tuple is immutable |    |
| A list is ordered collection of items  |  An array is ordered collection of items |  A tuple is an ordered collection of items  |
| List can store more than one data type  |  Array can store only **similar** data types |  Tuple can store more than one data type  | 
|Item in the list can be changed or replaced |Item in the array can be changed or replaced |Item in the tuple **cannot** be changed or replaced
---
![img](/assets/img/checkpoint.jpg) 
What we have learned so far:
> 1. What are arrays, lists, and tuples
> 2. Basic operations to create, access, traverse, insert, update, delete, and search

Knowledge Check:
> Why might we use an array instead of a list? 
---
##### Dictionary, Set, and Map

In computing, we sometimes need to work with data in a way that allows us to maintain or create an association between objects. A **hash table** (sometimes called a **hash map** or **associative array**) is a data structure that implements this association.

> What are hash tables?
> - A hash table uses a *hash function* to compute an *index* (or hash code) for a data element. This makes accessing the data faster as the index value behaves as a key for the data value. In other words, hash tables store key-value pairs but the key is generated through a hashing function. 
> - A **hashing function** is an integer of fixed length code, which represents a key to identify data.
> - Sometimes, the hash function can create **collisions**
> - When storing a new item into a hash table and a hash collision occurs, but the actual keys themselves are different, the hash table stores both items (as a list). However, if the key of the new item matches the key of an old item, the hash table will erase the old item and overwrite it with the new item, so every item in the table has a unique key.<br>
![img](/assets/img/confusion.jfif)

Example of Collision in a Hash Table using names and phone numbers
![img](/assets/img/hashmap.png)

Python uses a **Dictionary** to represent hash tables. In a dictionary, the key is separated from its value by a colon `:`, the items are separated by commas, and the whole thing is enclosed in curly brackets `{key1:value1, key2:value2, key3:value3}`. An empty dictionary without any items is written with just two curly braces, like this `{}`.

**Keys** are unique within a dictionary while values may not be. The **values** of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

Basic Operations we can make with a dictionary:
> 1. **Traverse** − iterate through a dictionary
> 2. **Insertion** − add new key-value pairs to a dictionary
> 3. **Deletion** − delete elements or the entire contents of a dictionary
> 4. **Search** − sort and filter items in a dictionary
> 5. **Update** − update key-value pairs 

**Examples to try: Take 1 to 2 Minutes:**
The below examples cover how to create, access, insert, delete, update and search python dictionaries

**Traverse a python dictionary**
```python
# Create a dict 
dict1 = {
    'color': 'blue', 
    'fruit': 'apple', 
    'pet': 'dog'
}

# traverse items in a dict
for i in dict1.items():
    print(i)

# traverse keys in a dict
for k in dict1:
    print(k)

# traverse values in a dict
for v in dict1.values():
    print(v)

# traverse keys and values in a dict
for k,v in dict1.items():
    print("Key=", k)
    print("Value=", v)
```

Example 2: using arrays to create a dict with comprehension

A **dictionary comprehension** is a compact way to process all or part of the elements in a collection and return a dictionary as a results. In contrast, list comprehension need two expressions separated with a colon followed by for and if (optional) clauses. 

When a dictionary comprehension is run, the resulting key-value pairs are inserted into a new dictionary in the same order in which they were produced.

```python
# Two arrays that we need to associate using a dict
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']

# using comprehension in python is the same as using a for loop
a_dict = {key: value for key, value in zip(categories, objects)}

print(a_dict)
```
**Access values in a dictionary**
```python
# Access data in a python dictionary 
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# We access values by putting the key name in square brackets
print("dict1['Name']: ", dict1['Name'])
print("dict1['Age']: ", dict1['Age'])
```

**Insert items into a dictionary**
```python
# Create an empty dictionary
newDict = {}

# insert a new key-value pair
newDict['someKey'] = 'someValue'

print(newDict)
```

**Delete items in a dictionary**
```python
# Create a dictionary
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1)

# Use del to remove specific items from a dict
del dict1['Name'] # remove entry with key 'Name'
print(dict1)

# use clear() to remove all items from a dict
dict1.clear()     # remove all entries in dict
print(dict1)

# use del to delete the dict object 
del dict1
```
**Search items in a dictionary**
```python
# Create a dict of key-value pairs
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {}  # Create a new empty dictionary, outside the loop

# start traversal
for key, value in a_dict.items():
    # If value satisfies the condition, then store it in new_dict
    if value <= 2:
        new_dict[key] = value

# New dict contains items satisfying condition
new_dict
```
Example 2: Using Comprehension
```python
# Create a dict
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}

# use dict comprehension to filter based on a conditional 
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)
```

Example 3: Sorting a dict using Comprehension
```python

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}

sorted_income = {k: incomes[k] for k in sorted(incomes)}

print(sorted_income)
```
**Update items in a dictionary**
```python
# Create a dictionary 
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# The same operation to insert values to an empty dict 
# can be used to update an existing item

dict1['Age'] = 8; # update existing entry
dict1['School'] = "DPS School"; # Add new entry

print("dict1['Age']: ", dict1['Age'])
print("dict1['School']: ", dict1['School'])
```
A **Set** is a collection of items not in any particular order. A Python set has several characteristics and conditions:
> The elements in the set cannot be duplicates.
> The elements in the set are immutable (cannot be modified) but the set as a whole is mutable.
> There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

The sets in python <u>are typically used for mathematical operations like union, intersection, difference and comparison. </u> Set items are unordered, unchangeable, and do not allow duplicate values. 

Set Operations
Basic Operations we can make with a set:
> 1. **Traverse** − iterate through a set
> 2. **Insertion** − add elements to a set
> 3. **Deletion** − remove elements from a set
> 4. **Union** − combining sets
> 5. **Intersection** − find common elements between sets
> 6. **Difference** − find difference between sets
> 7. **Compare** - find if one set is a subset or superset of another

**Examples to try: Take 1 to 2 Minutes:**
The below examples cover how to use set operations

**Access elements in a set**
```python
# Create a set
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

# Traverse the set to access its elements
for d in Days:
   print(d)
```
**Insert elements in a set**
```python
# Create a set
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

# Use add() to append new elements to a set
Days.add("Sun")
print(Days)
```
**Delete elements in a set**
```python
# Create a set
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
# use discard() to remove a specific element from a set
Days.discard("Sun")
print(Days)

# del deletes the entire set 
del Days
```
**Union of multiple sets**
```python
# Create two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])

# use the pipe | to combine sets
AllDays = DaysA | DaysB
print(AllDays)
```
**Intersection of multiple sets**
```python
# Create two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])

# Use the & operator to find which values intersect both sets
AllDays = DaysA & DaysB

# elements both sets have in common
print(AllDays)
```
**Difference between multiple sets**
```python
# Create two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])

# Use - to find the difference between the first set from the second
AllDays = DaysA - DaysB

# elements that are in the first set but not the second
print(AllDays)
```
**Comparison of multiple sets**
```python
# Create two sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

# use <= to see if set A is a subset of set b, result is boolean
SubsetRes = DaysA <= DaysB
print(SubsetRes)

# use >= to see if set b is a superset of set a, result is boolean
SupersetRes = DaysB >= DaysA
print(SupersetRes)
```

A Python **Maps**, also called a `ChainMap` is a type of data structure to manage multiple dictionaries together as one unit. The combined dictionary contains the key and value pairs in a specific sequence eliminating any duplicate keys. The best use of ChainMap is to search through multiple dictionaries at a time and get the proper key-value pair mapping. We also see that these ChainMaps behave as stack data structure.

**Note**: python `map()` is not the same as `ChainMap()`

Common ChainMap methods:
`keys()` : used to display all the keys of all the dictionaries in ChainMap.

`values()` : used to display values of all the dictionaries in ChainMap.

`maps()` : used to display keys with corresponding values of all the dictionaries in ChainMap.

`new_child()` : adds a new dictionary in the beginning of the ChainMap.

`reversed()` : reverses the relative ordering of dictionaries in the ChainMap

ChainMap Operations
> 1. **Create** − create chain map from dictionaries
> 2. **Insertion** - Update a chain map 
> 3. **Reverse** - Reverse dictionaries in a chain map
> 4. **Deletion** - Delete a chain map

**Examples to try: Take 1 to 2 Minutes:**
The below examples cover how to use chainMap operations

**Creating a ChainMap**
```python
import collections

# Create two dicts
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

# Create a chain map ChainMap() from collections
res = collections.ChainMap(dict1, dict2)
print(res)

# Creating a single dictionary
print(res.maps,'\n')

# print all the keys and values from the chain map
# Note if there are duplicate keys only the first is preserved
print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))

# Print all the elements from the result
print('elements:')
for key, val in res.items():
   print('{} = {}'.format(key, val))


# Find a specific value in the result, returns boolean
print('day1 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))
```
**Insert a new dict into a ChainMap**
```python
import collections
  
# initializing dictionaries
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }
dict3 = { 'f' : 5 }
  
# initializing ChainMap with dic1 and dic2
chain = collections.ChainMap(dict1, dict2)
  
# printing chainMap using map
print ("All the ChainMap contents are : ")
print (chain.maps)
  
# using new_child() to add new dictionary dict3
chain1 = chain.new_child(dict3)
  
# printing chainMap using map
print ("Displaying new ChainMap : ")
print (chain1.maps)
```

**Reverse a ChainMap**
```python
import collections
  
# initializing dictionaries
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }
  
# initializing ChainMap with dict1 and dict2
chain = collections.ChainMap(dict1, dict2)
  
# printing chainMap using map
print ("All the ChainMap contents are : ")
print (chain.maps)
  
  
# displaying value associated with b before reversing
print ("Value associated with b before reversing is : ",end="")
print(chain['b'])
  
# reversing the ChainMap
chain.maps = reversed(chain1.maps)
  
# displaying value associated with b after reversing
print ("Value associated with b after reversing is : ",end="")
print (chain['b'])
```
**Delete a ChainMap**
```python
import collections
  
# initializing dictionaries
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }
  
# initializing ChainMap with dict1 and dict2
chain = collections.ChainMap(dict1, dict2)

# delete the chain map
del chain
```


---
![img](/assets/img/checkpoint.jpg) 
What we have learned so far:
> 1. What are Dictionaries and their basic operations
> 2. What are Sets and their basic operations
> 3. What are Maps and their basic operations

Knowledge Check:
> How do we get a single set of distinct elements from two sets that contain overlapping items?
