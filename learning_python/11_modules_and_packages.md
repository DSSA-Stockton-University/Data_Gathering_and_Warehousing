# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 10

---
# Modules and Packages in Python

![img](/assets/img/module.png)

---

#### Python Modules:
A __Module__ consist of any related functions, classes, or variables that are stored in a `.py` file that is not the main script to be executed. 

Modules help improve the development process by focusing on a small number of tasks.

Modules Summary:
- Allow users to develop functionality to be used in different parts of an application
- Minimize duplicate code
- Minimize interdependency
- Focus on a small set of particular tasks

#### Python Packages
A __Package__ is a directory or collection of modules. 

Packages have a hierarchical structure of the module namespace. For a `.py` file to be considered a package. In other words, 


Example of Modules and Packages using `import`
```python
# from datetime is the library containing modules
# import datetime will import the datetime module
from datetime import datetime

# Pyspark is the package
# functions is module
# lead is a function from the functions module
from pyspark.sql.functions import lead
```

##### Creating a Module

To create a module we only need to save the below function to a `.py` file
```python
def greeting(name):
  print("Hello, " + name)
```

###### Using a Module
```python
# We use the name of the .py file to reference the module
from mymodule import greeting

greeting("Tim")
```

###### Renaming a Module
```python
# We use the "as" to rename modules
import mymodule as mm
```

###### Listing all named objects in a module
```python
import platform

x = dir(platform)
print(x)
# This work for user defined modules as well
```