# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 9

---
# Metaprogramming in Python

![img](/assets/img/crisis.jpg)

---

The process of adding functionality to an existing function with decorators is called __metaprogramming__.

__Decorators__ allow developers to modify the behavior of a function or class. Decorators wrap a function without permanently modifying it. When using python decorators, a function can take another function as an argument (the function to be decorated) and return the same function with or without extending functionality.


Example:
__Passing the function as an argument__
```python
def makeUpperCase(text):
    return text.upper()
 
def makeLowerCase(text):
    return text.lower()
 
# In this example HelloWorld is the decorator
def HelloWorld(func):
    # storing the function in a variable
    greeting = func("""Hello, World!""")
    # The print line extends func
    print (greeting)
 
HellowWorld(makeUpperCase)
HellowWorld(makeLowerCase)
```
Output:
```
HELLO, WORLD!
hello, world!
```
A decorator takes a function, extends it and returns. 

```python
# In this case hello is the decorator
def hello(func):                                    
    def inner():                                        
        print("Hello ")                                    
        func()                                             
    return inner                                          

# Name is the function to be extended
def name():
    print("Alice")
               
obj = hello(name)                                 
obj()  
```
The function `name()` is decorated by the function `hello()`. It wraps the function in the other function.
![img](/assets/img/python-decorator.png)


__Using a decorator to pretty print a sum function__
```python
# We define the decorator and the extended functionality 
def pretty_sum(func):
    def inner(a,b):
        print(str(a) + " + " + str(b) + " is ", end="")
        return func(a,b)                                   
    return inner

# We can use the @ character to wrap our sum function
@pretty_sum
def sum(a,b):
    summed = a + b
    print(summed)                                       
                                                 
if __name__ == "__main__":           
    sum(5,3)  
```

__Using a decorator with additional arguments__

```python
def my_decorator(msg='hi'):
    def this_is_Decorated(func):
        def wrapper():
            print(msg)
            print("Functionality Added Inside the decorator, before calling the function")
            func()
            print("Functionality Added Inside the decorator, after calling the function")
        return wrapper   # decorator needs to return a function
    return this_is_Decorated

@my_decorator(msg='hello')
def printName():
    print("Stockton")

printName()
```
Output
```
hello
Functionality Added Inside the decorator, before calling the function
Stockton
Functionality Added Inside the decorator, after calling the function
```