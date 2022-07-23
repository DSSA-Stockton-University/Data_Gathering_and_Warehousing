# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2022
**Module**: 1
**Week**: 5

---
![img](/assets/img/headache.jfif)

---
## Iterators in Python

**Iterators** are objects that you can iterate on, which returns one object at a time. Iterators allow us to __traverse__ through all values in a set. 

In Python, an object that implements the iterator protocol consists of the methods __iter__() and __next__(). To create a Python iterator object, you will need to implement these two methods in your iterator class.

* __iter__: This returns the iterator object itself and is used while using the “for” and “in” keywords.
* __next__: This returns the next value. This would return the `StopIteration error` once all the objects have been looped through.

#### FOR loop implementation
Internally, the for loop creates an _iterator object_ and accesses it's values one by one until the StopIteration exception is raised. This is how a for loop is internally implemented.

The for loop is internally using the iterator protocol with an exception handling condition to iterate over iterables and accessing their values.
```python

# Interestingly, the for loop is actually a while loop in disguise!
iter_obj = iter(iterable)
while True:
    try:
        element(next(iter_obj))
    except StopIteration:
        break
```


**Benefits of Iterators**
Iterators are best known for saving resources. Only one element is stored in the memory at a time. If it wasn't for iterators and should we have used lists, all the values would've been stored at once, which means more memory and less efficient.

This can come in handy at almost all types of applications, ranging from web applications to AI and neural network models. **Whenever we are thinking about minimizing memory usage, we can always resort to iterators.**



**Exercise:** Should only take 1-2 minutes...
1. Try using the example below to write your own iterator

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
```

Lets look at another example but using a string
**Remember strings are sequences in python**
```python
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
```
The same example as the first one but represented as a `for loop`
```python
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
```

---

## Generators in Python

*Generators** are somewhat similar to iterators but the main difference is that iterators use `return` while generators use the keyword `yield` instead. 

Generator are dedicated in python for generating a sequence of values of _any data type_. The generator let us process only one value at a time and not store the entire values of the sequence into the memory. This can be very useful while processing or dealing with very large numbers or big files.

Using `yield` in a generator is what gives it the edge over iterators. The `yield` keyword allows the generator function to pause and store the state of current variables (this is why iterators are more memory-efficient) so that we can resume the generator function again anytime we need. 

**Basic example of a generator**
```python
def gen(n):
    for i in range(n):
        yield i**2
```

**Notice** When we try to use the generator we only see it as an object. This is because we need to iterate over the generator 
```python
>>> g = gen(100000)
>>> g
<generator object gen at 0x7f86cc3e49e0>
```

Iterating over the generator object looks like this
```python
for i in g:
    print(i)
```

#### Benefits of generators

**Working with data streams or large files**
 - Usually for large csv files for example, we'd use a library like csv_reader. However, the amount of computation needed for extremely large files would probably exceed your memory resources. We can instead have the rows of the file separately stored into an array or have the count of the rows instantly available.
 
`csv_reader` will probably fail at counting large number of rows, but with this is easy with generators using yield statement.

**Large CSV files will consume all available memory**
```python
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```
```python
Traceback (most recent call last):
  File "ex1_naive.py", line 22, in <module>
    main()
  File "ex1_naive.py", line 13, in main
    csv_gen = csv_reader("file.txt")
  File "ex1_naive.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```
**We can work around this by using a generator to return each row at a time**
```python
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

**Generating Infinite Sequences**
 - Since your computer memory is finite, an infinite sequence will definitely use all of it. Generators can be used for an infinite sequence without consuming all memory.

```python
def infinite_sequence():
  num = 0
  while True:
      yield num
      num += 1
```

Let’s summarize the whole idea of Generator and Iterators..



#### Comparison between iterators and generators
**How to remember the difference between an iterator & generator**
* In iterators, we need to make use of the iterator protocol methods (`iter()` and `next()`) but generators are simpler as we only need to use a function.
* Generators are faster than iterators but iterators are more memory-efficient.
* In the case of Generators, the `yield` statement pauses the function and saves the state of that function.
* In the case of Iterators, the `return` statement immediately terminates and you can not do anything inside the function.

![img](/assets/img/iter.png)
