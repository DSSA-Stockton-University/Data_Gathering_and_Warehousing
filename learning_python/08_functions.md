# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 7

---
![img](/assets/img/python.jfif)

---

### What are Python Functions?

A __Function__ is a block of related statements designed to perform a task. Functions can be both built-in or user-defined and are designed to help a program be concise, non-repetitive, and organized. 

__built-in__ are functions that are built into python
__user-defined__ are functions built by users themselves.

#### How to define a Function?
* In order to create a function in python we need to use the `def` keyword. 
* Then the function must be given a name
* A function may use arguments 
* A function may use a return statement
* Statements inside a function must be indented (4 spaces)

Functions may create variables. If a function creates a variable it is not accessible outside of the function, hence it has _local scope_

variables inside a function only exist when the function is executed and are discarded when the function is returned or ends

A user may retain variables from a function if it is made part of the return statement. 

__A simple python function__
```python
# Make use of def and give a unique name
def my_func(x):
    # This is the statement
    print(x)
```
##### Arguments
Function Arguments can be default or optional. 

__Default Arguments__ are parameters that use a default value if one is not provided when the function is called. 

If a function uses default arguments, all additional arguments to the right must also have default values

```python
# The default value of x is set to 40
def some_func(x=40)
    print("x: ", x)
```

__Keyword Arguments__ are parameters that allow users to specify the argument's value.

```python
def some_func(x, y, z):
    print(x, y, z)

my_func(x="Hello", y="World", z=",")
# We can specify keyword args out of order
my_func(z="Hello", y="World", x=",")
```


__Variable Length Arguments__ are used when we are to pass `n` number of arguments to a function using wildcards `*` or `**`

* `*` are for non-keyword arguments
* `**` are for key-words arguments

__*args__ in function definitions allows us to pass a variable number of non-keyword arguments to a function.

__Note__: python understands the symbol `*` to take variable length arguments but it is common convention to provide `args` as the naming convention.`*args` allows us to take in more arguments than the number of formal arguments defined. 

```python

# *args could be called *anything
def some_func(*args):
    for a in arg:
        print(arg)
# We can use any variable list of non-keyword arguments
some_func(2, 4, 5, 6, 7)
```


__**kwargs__  in a function definition is used to pass a keyword variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

A _keyword argument_ is where you provide a name to the variable as you pass it into the function.

One can think of the **kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

```python
# **kwargs could be called **anything
def some_func(**kwargs):
    for k, v in kwargs:
        print(f"{k} == {v}")


some_func(apple='fruit', carrot='vegetable')
```

__Docstrings__ are used to describe the functionality of a python function. 

```python
def some_func(x):
    """
    This function prints the value of x
    """
    print(x)

# we can access docstrings of a function using
print(some_func.__doc__)
```
__lambda or Anonymous functions__ are python functions without a name. Where `def` is used to define normal functions `lambda` is used create anonymous functions. 

__lambda__ functions can have any number of arguments but only one expression which is evaluated then returned.

How to setup a lambda function
`lambda args: expression`

```python
# Setting up a lambda function
solution = lambda x, y: x + y

print(solution(2,2))
```

