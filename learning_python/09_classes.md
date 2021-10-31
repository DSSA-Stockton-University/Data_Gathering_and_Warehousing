# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 8

---
# Working with Classes in Python

![img](/assets/img/stop.jfif)

---

A Python __class__ is a blueprint from which objects are created. An __object__ is a collection of data (variables) and methods (functions). A class provides a way of building data and functionality together. Classes let developer's do a few things:
1. Creating a new class creates a new type of object, allowing new instances of that type to be made. 
2. Each class instance can have attributes attached to it for maintaining its state. 
3. Class instances can also have methods (defined by their class) for modifying their state.

#### Define a Python Class

To define a function in python we use `def`, to define python classes we use the `class` keyword. The below line creates a python class then created a new instance of the class by calling it.

```python
# Defines the class
class SomeObject:
    """
    The first string inside of a class is called a docstring
    """
    pass

# Creates a new instances of the class
obj = SomeObject()
```

#### Adding Attributes to a Python Class

Adding attributes to a class is the same as creating variables

```python
# Defines the class
class SomeObject:
    """
    The first string inside of a class is called a docstring
    """

    # Lets add some attributes to the class
    someAttribute = 40
    anotherAttribute = "This is an attribute"
    _encapsulatedAttribute = "Cannot be modified"

# Creates a new instances of the class
obj = SomeObject()
```

#### Adding Methods to a Python Class
A Method is a essentially a python function that is tied to the class instance. 

```python
# Defines the class
class SomeObject:
    """
    The first string inside of a class is called a docstring
    """

    # Lets add some attributes to the class
    someAttribute = 40
    anotherAttribute = "This is an attribute"
    _encapsulatedAttribute = "Cannot be modified"

    # This is a method that prints two attributes
    def printStrings(self):
        print(self.anotherAttribute, _encapsulatedAttribute)
```

#### Constructors in Python Classes

Class functions that begin with double underscore __ are called special functions as they have special meaning.

One common constructor is the __init__() function. This special function gets called whenever a new object of that class is instantiated. `__init__()` is normally use it to initialize all the attributes (variables).


The below example creates a class with two attributes name and age using the `__init__()` constructor
```python
# Create a class called person
class Person:
    """
    This class is used to create objects
     of a persons first name and age
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creates a new instances of the class
p = Person("John", 36)

# Print the new instances attributes
print(p.name)
print(p.age)
```

#### The `self` Argument
The self argument is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

```python
# Create a class called person
class Person:
    """
    This class is used to create objects
     of a persons first name and age
    """

    def __init__(someName, name, age):
        someName.name = name
        someName.age = age

# Creates a new instances of the class
p = Person("John", 36)

# Print the new instances attributes
print(p.name)
print(p.age)
```

#### Modify Class Attributes or Delete the Class
We can modify class attributes in the same way we can modify variables

```python
# Create a class called person
class Person:
    """
    This class is used to create objects
     of a persons first name and age
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creates a new instances of the class
p = Person("John", 36)

# Print the new instances attributes
print(p.age)

# Modify the attributes value and print again
p.age = 40
print(p.age)

# Delete the instance
del p

```

#### The `pass` Statement
class definitions cannot be empty, but often we need to create a placeholder for code or functionality to be added later. Put in the pass statement to avoid getting an error.

```python
class Person:
    pass
```

#### Other built in attributes of Python Classes

Along with the other attributes, a Python class also contains some built-in class attributes which provide information about the class.

| **Num** | **Attribute** | **Description** |
|---|---|---|
| 1 | \_\_dict\_\_ | It provides the dictionary containing the information about the class namespace\. |
| 2 | \_\_doc\_\_ | It contains a string which has the class documentation |
| 3 | \_\_name\_\_ | It is used to access the class name\. |
| 4 | \_\_module\_\_ | It is used to access the module in which, this class is defined\. |
| 5 | \_\_bases\_\_ | It contains a tuple including all base classes\. |


```python
class Student:    

    def __init__(self,name,id,age):    
        self.name = name    
        self.id = id    
        self.age = age    

    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))    

s = Student("John",101,22)    
print(s.__doc__)    
print(s.__dict__)    
print(s.__module__)    
```
Returns
```
None
{'name': 'John', 'id': 101, 'age': 22}
__main__
```
