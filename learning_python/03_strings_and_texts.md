# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 1

---
## Working with Strings & Text

![img](/assets/img/regex.png)
---

**Regular Expressions** are a versatile tool for text processing. In python, regular expressions are included as part of standard library called `re`. Regular expressions are specialized for text processing. Parts of a regular expression can be saved for future use, analogous to variables and functions. 
 - There are ways to perform AND, OR, NOT conditionals using regular expressions. 
 - Additionally, there are operations similar to range function, string repetition operator and so on.

The `str` class comes loaded with variety of methods to deal with text.   

**Common Ways Regular Expressions are Used:**
> 1. Sanitizing a string to ensure that it satisfies a known set of rules. For example, to check if a given string matches password rules.
> 2. Filtering or extracting portions of alphabets, numbers, punctuation etc from abstract text.
> 3. Qualified string replacement. For example, replacing text at the start or the end of a string, or only whole words, based on surrounding text.

---
#### Python `re` introduction

##### re module documentation

It is always a good idea to know where to find the documentation. The default offering for Python regular expressions is the `re` standard library module. 
Visit [docs.python: re](https://docs.python.org/3/library/re.html) for information on available methods, syntax, features, examples and more. Here's a quote:

>A regular expression (or RE) specifies a set of strings that matches it; the functions in this python module let you check if a particular string matches a given regular expression

##### Using `re.search()`

Normally you'd use the `in` operator to test whether a string is part of another string or not. For regular expressions, use the `re.search` function whose argument list is shown below.

>`re.search(pattern, string, flags=0)`

The first argument is the RE pattern you want to test against the input string, which is the second argument. `flags` is optional, it helps to change the default behavior of RE patterns. 

The return value of `re.search` function is a `re.Match` object when a match is found and `None` otherwise

Note: As a good practice, always use **raw strings** to construct the RE pattern.

```python
>>> sentence = 'This is a sample string'

# check if 'sentence' contains the given search string
>>> 'is' in sentence
True
>>> 'xyz' in sentence
False

# need to load the re module before use
>>> import re

# check if 'sentence' contains the pattern described by RE argument
>>> bool(re.search(r'is', sentence))
True
>>> bool(re.search(r'xyz', sentence))
False
```

Note: Before using the `re` module, you need to `import` it. 

Here's an example with `flags` optional argument.

```python
>>> sentence = 'This is a sample string'

>>> bool(re.search(r'this', sentence))
False

# re.IGNORECASE (or re.I) is a flag to enable case insensitive matching
>>> bool(re.search(r'this', sentence, flags=re.I))
True
```

##### Using `re.search()` in conditional expressions

As Python evaluates `None` as `False` in boolean context, `re.search` can be used directly in conditional expressions. 
```python
>>> sentence = 'This is a sample string'
>>> if re.search(r'ring', sentence):
...     print('mission success')
... 
mission success

>>> if not re.search(r'xyz', sentence):
...     print('mission failed')
... 
mission failed
```

Here's some generator expression examples using list comprehension.

```ruby
>>> words = ['cat', 'attempt', 'tattle']

>>> [w for w in words if re.search(r'tt', w)]
['attempt', 'tattle']

>>> all(re.search(r'at', w) for w in words)
True

>>> any(re.search(r'stat', w) for w in words)
False
```

##### Using `re.sub()`

For normal search and replace, you'd use the `str.replace` method. For regular expressions, use the `re.sub` function, whose argument list is shown below.

>`re.sub(pattern, repl, string, count=0, flags=0)`

 - The first argument is the RE pattern to match against the input string, which is the third argument.
 - The second argument specifies the string which will replace the portions matched by the RE pattern. 
 - The third argument is the string to be evaluated
 - `count` and `flags` are optional arguments.

```python
>>> greeting = 'Have a nice weekend'

# replace all occurrences of 'e' with 'E'
# same as: greeting.replace('e', 'E')
>>> re.sub(r'e', 'E', greeting)
'HavE a nicE wEEkEnd'

# replace first two occurrences of 'e' with 'E'
# same as: greeting.replace('e', 'E', 2)
>>> re.sub(r'e', 'E', greeting, count=2)
'HavE a nicE weekend'
```

##### Compiling regular expressions

Regular expressions can be compiled using `re.compile` function, which returns a `re.Pattern` object.

>`re.compile(pattern, flags=0)`

The top level `re` module functions are all available as methods for such objects. Compiling a regular expression is useful if the RE has to be used in multiple places or called upon multiple times inside a loop (speed benefit).

```python
>>> pet = re.compile(r'dog')
>>> type(pet)
<class 're.Pattern'>

# note that 'search' is called upon 'pet' which is a 're.Pattern' object
# since 'pet' has the RE information, you only need to pass input string
>>> bool(pet.search('They bought a dog'))
True
>>> bool(pet.search('A cat crossed their path'))
False

# replace all occurrences of 'dog' with 'cat'
>>> pet.sub('cat', 'They bought a dog')
'They bought a cat'
```

Some of the methods available for compiled patterns also accept more arguments than those available for top level functions of the `re` module. For example, the `search` method on a compiled pattern has two optional arguments to specify **start** and **end** index positions. Similar to `range` function and slicing notation, the ending index has to be specified `1` greater than desired index.

>`Pattern.search(string[, pos[, endpos]])`

Note that there's no `flags` option as that has to be specified with `re.compile`.

```ruby
>>> sentence = 'This is a sample string'
>>> word = re.compile(r'is')

# search for 'is' starting from 5th character of 'sentence' variable
>>> bool(word.search(sentence, 4))
True

# search for 'is' starting from 7th character of 'sentence' variable
>>> bool(word.search(sentence, 6))
False

# search for 'is' between 3rd and 4th characters
>>> bool(word.search(sentence, 2, 4))
True
```

##### Using `re` with `bytes`

To work with `bytes` data type, the RE must be of `bytes` data as well. Similar to `str`, RE uses a **raw** format to construct a `bytes`.

**This causes an error**
```python
>>> byte_data = b'This is a sample string'

# error message truncated for presentation purposes
>>> re.search(r'is', byte_data)
TypeError: cannot use a string pattern on a bytes-like object
```

**This does not**
```python
# use rb'..' for constructing bytes pattern
>>> bool(re.search(rb'is', byte_data))
True
>>> bool(re.search(rb'xyz', byte_data))
False
```

## Summary

| Note    | Description |
| ------- | ----------- |
| [docs.python: re](https://docs.python.org/3/library/re.html) | Python standard module for regular expressions |
| `re.search` | Check if given pattern is present anywhere in input string |
|  | `re.search(pattern, string, flags=0)` |
|  | Output is a `re.Match` object, usable in conditional expressions |
|  | raw strings preferred to define RE |
|  | Additionally, Python maintains a small cache of recent RE |
| `re.sub` | search and replace using RE |
|  | `re.sub(pattern, repl, string, count=0, flags=0)` |
| `re.compile` | Compile a pattern for reuse, output is a `re.Pattern` object |
|  | `re.compile(pattern, flags=0)` |
| `rb'pattern'` | Use byte pattern for byte input |
| `re.IGNORECASE` or `re.I` | flag to ignore case while matching |
