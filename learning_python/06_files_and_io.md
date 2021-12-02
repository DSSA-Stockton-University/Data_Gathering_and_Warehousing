# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 5

---
![img](/assets/img/birdmeme.jpg)

---

#### Working with Files in python

__Files__ are named locations on disk that store information. They are used to permanently store data so it can be accessed later in the future. 

In python, when we want to _read_ or _write_ to a file we need to do a few operations:
- Open the file
- Perform some operation
- Close the file

__Opening Files in python__
Python has a built-in function called `open()` that is used for opening files. The function returns a file object called a _handle_ because it is used to read or modify the file. `open()` supports several modes for handling files: 

|Mode|Description|
|:----|:----|
|r|Opens a file for reading. (default)|
|w|Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.|
|x|Opens a file for exclusive creation. If the file already exists, the operation fails.|
|a|Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.|
|t|Opens in text mode. (default)|
|b|Opens in binary mode.|
|+|Opens a file for updating (reading and writing)|

Here are some examples of using `open()` wi
```python
f = open("test.txt") # equivalent to 'r' or 'rt'
f = open("test.txt", mode='w')  # write in text mode
f = open("img.bmp", mode ='r+b') # read and write in binary mode.
```

__File Encodings__ also known as character encodings, specify how to represent characters when text processing. One encoding may be preferable over another in terms of which language characters it can or cannot handle, although Unicode is usually preferred

When reading from or writing to files, improperly matching file encodings may result in exceptions or incorrect results

__UTF-8__  is a _Unicode character encoding_ method. UTF-8 takes a given Unicode character and translates it into a string of binary. It also does the reverse, reading in binary digits and converting them back to characters.

Moreover, the default encoding is platform dependent. In windows, it is `cp1252` but `utf-8` in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

```python
f = open("test.txt", mode='r', encoding='utf-8')
```

__Closing Files in python__

When we are done performing operations on a file, we need to close it. This is done using `close()` method in python.

Using `close()` guarantees that the file is properly closed even if an exception is raised

__Example of close():__
```python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```

__Example of close() with try & finally statements:__
```python
try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```

The best way to close files is using the `with` statement in python. `with` executes the `close()` method internally, so it does not need to be called explicitly.

__Using `with` statement to work with files__

Example for reading data
```python
with open('data.txt', mode='r', encoding='utf-8') as f:
    data = f.read()
```

Example for writing data
```python
with open('data.txt', mode='w', encoding='utf-8') as f:
    data = "Some data I need to write to a file"
    f.write(data)
```

__Writing Files__

When writing files we need to use `open()` with modes `w`, `a` or `x`. 

If we are writing multiple lines to a file we need to include the newline characters as part of the string using `\n`

To write strings or sequences to a file we use the `write()` method in python

__Example of creating a mult-line file using `write()`__
```python
# Note: because the mode is 'w', the file will be overwritten each time
# this line of code is executed
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
```

__Using `read()` to read the data of a file__

`read(size)` is a method with a single argument called size. Size specifies the amount of data to read, if it is not specified, it will read to the end of the file. 

```python
>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
```

We can change our position within a file using a method called `seek()` and get our current position using a method called `tell()` 

```python
>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines
```

We can use a `for` loop to read through a file
```python
>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines
```

We can also use `readline()` to read each line of a file
```python
>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''
```


List of file methods in python:
|Method|Description|
|:----|:----|
|close()|Closes an opened file. It has no effect if the file is already closed.|
|detach()|Separates the underlying binary buffer from the TextIOBase and returns it.|
|fileno()|Returns an integer number (file descriptor) of the file.|
|flush()|Flushes the write buffer of the file stream.|
|isatty()|Returns True if the file stream is interactive.|
|read(n)|Reads at most n characters from the file. Reads till end of file if it is negative or None.|
|readable()|Returns True if the file stream can be read from.|
|readline(n=-1)|Reads and returns one line from the file. Reads in at most n bytes if specified.|
|readlines(n=-1)|Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.|
|seek(offset,from=SEEK_SET)|Changes the file position to offset bytes, in reference to from (start, current, end).|
|seekable()|Returns True if the file stream supports random access.|
|tell()|Returns the current file location.|
|truncate(size=None)|Resizes the file stream to size bytes. If size is not specified, resizes to current location.|
|writable()|Returns True if the file stream can be written to.|
|write(s)|Writes the string s to the file and returns the number of characters written.|
|writelines(lines)|Writes a list of lines to the file.|

---

#### Working with Directories in python

the python `os` module is part of the standard library and has a number of useful functions for working with file directories. 

__Listing all the files in a directory__

`os.listdir()` returns a Python list containing the names of the files and subdirectories in the directory given by the path argument:

```python
>>> import os
>>> entries = os.listdir('my_directory/')
['sub_dir_c', 'file1.py', 'sub_dir_b', 'file3.txt', 'file2.csv', 'sub_dir']
```

__Listing all subdirectory files__

Sometimes we want to list all the files in a subdirectory. `os.path` gives us a variety of methods for handling this like the example below: 

```python
import os

# List all subdirectories using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)
```

Since python 3.5 we can do this more efficiently by using the `scandir()` method of `os`:
```python
import os

# List all subdirectories using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
```

__Working with file meta data__

Sometimes we want to find or process files that have recently been modified or are of a certain size. `stat()` provides a few methods for doing this:

```python
>>> import os
>>> with os.scandir('my_directory/') as dir_contents:
...     for entry in dir_contents:
...         info = entry.stat()
...         print(info.st_mtime) # Notice time is in unix representing time in seconds since the epoch
...
1539032199.0052035
1539032469.6324475
1538998552.2402923
1540233322.4009316
1537192240.0497339
1540266380.3434134
```

__Making directories__

`os` gives us a couple ways of making new directories in python. If using `mkdir()` a `FileExistsError` will be raised if a directory already exists.

|Function|Description|
|:----|:----|
|os.mkdir()|Creates a single subdirectory|
|os.makedirs()|Creates multiple directories, including intermediate directories|

__Example creating a new directory__
```python
import os

p = 'new_directory/'
os.mkdir(p)
```
__Example creating a directory with subdirectories__
```python
import os

p = '2021/10/05'
os.mkdir(p)
```

```python
.
|
└── 2021/
    └── 10/
        └── 05/
```


__Using Pattern Matching with Filenames__

After getting a list of files from a directory sometimes we want only specific files. Python offers us a couple ways of pattern matching files:

- `endswith()` and `startswith()` string methods
- `fnmatch.fnmatch()`
- `glob.glob()`

__Example using string methods__
```python
>>> import os

>>> # Get .txt files
>>> for f_name in os.listdir('some_directory'):
...     if f_name.endswith('.txt'):
...         print(f_name)
```

```bash
data_01.txt
data_03.txt
data_03_backup.txt
data_02_backup.txt
data_02.txt
data_01_backup.txt
```

__Example using glob__
```python
>>> import glob
>>> glob.glob('*.py')
['admin.py', 'tests.py']
```
__glob__ allows for shell style wildcards to be used in the pattern match. In this way, we can find all the python files by the `.py` extension.


__Making Temporary files__

Sometimes we need to store data temporarily in a file while a program is running. `tempfile` provides a handle for creating and deleting temporary files once the program is finished.

Using the `TemporaryFile` from `tempfile` module qill create a file like object using the same modes we normally would use with `open()`

Temporary files do not require names because they are destroyed at the end of the program. 

```python
from tempfile import TemporaryFile

# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')
fp.write('Hello World')

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()

# Close the file, after which it will be removed
fp.close()
```

__Deleting Files & Directories in python__

`os` gives us several methods for removing files, such as, `os.remove()` and `os.unlink()`

Calling `unlink()` or `remove()` on a file deletes the file from the filesystem. These two functions will throw an `OSError` if the path passed to them points to a directory instead of a file. 

```python
import os

data_file = 'home/data.txt'

# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')
```

To delete a directory we can use `os.rmdir()`. Please note that in order to delete the directory, the directory must first be empty.

```python
from pathlib import Path

trash_dir = Path('my_documents/bad_dir')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```

To delete a non-empty directory we must use `shutil`

```python
import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
```
|Function|Description|
|:----|:----|
|os.remove()|Deletes a file and does not delete directories|
|os.unlink()|Is identical to os.remove() and deletes a single file|
|os.rmdir()|Deletes an empty directory|
|shutil.rmtree()|Deletes entire directory tree and can be used to delete non-empty directories|

__Copying Files in Python__

`shutil` gives us a few functions for copying files. The most commonly used functions are `shutil.copy()` and `shutil.copy2()`. 

```python
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy2(src, dst)
```

Using `copy2()` preserves details about the file such as last access time, permission bits, last modification time, and flags.

```python
import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)
```

To move a file or directory to another location, use `shutil.move(src, dst)`.

```python
>>> import shutil
>>> shutil.move('dir_1/', 'backup/')
'backup'
```


__Renaming Files in python__

We can rename a file using `os.rename()`

```python
os.rename('first.zip', 'first_01.zip')
```


__Working with Archives and Compressed Files__

`zipfile` module is part of the Python Standard Library and has functions that make it easy to open and extract ZIP files.

To read the contents of a ZIP file, the first thing to do is to create a ZipFile object. ZipFile objects are similar to file objects created using open(). ZipFile is also a context manager and therefore supports the with statement:

```python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
```

To get a list of files in the archive, call `namelist()` on the ZipFile object:

```python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    zipobj.namelist()
```

```bash
['file1.py', 'file2.py', 'file3.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
```

The zipfile module allows you to extract one or more files from ZIP archives through `extract()` and `extractall()`.

```python
>>> import zipfile
>>> import os

>>> os.listdir('.')
['data.zip']

>>> data_zip = zipfile.ZipFile('data.zip', 'r')

>>> # Extract a single file to current directory
>>> data_zip.extract('file1.py')
'/home/terra/test/dir1/zip_extract/file1.py'

>>> os.listdir('.')
['file1.py', 'data.zip']

>>> # Extract all files into a different directory
>>> data_zip.extractall(path='extract_dir/')

>>> os.listdir('.')
['file1.py', 'extract_dir', 'data.zip']

>>> os.listdir('extract_dir')
['file1.py', 'file3.py', 'file2.py', 'sub_dir']

>>> data_zip.close()
```


Creating a new zipfile archive and adding files
```python

>>> import zipfile

>>> file_list = ['file1.py', 'sub_dir/', 'sub_dir/bar.py', 'sub_dir/foo.py']
>>> with zipfile.ZipFile('new.zip', 'w') as new_zip:
        for name in file_list:
            new_zip.write(name)
```

TAR files are uncompressed file archives like ZIP. They can be compressed using `gzip`, `bzip2`, and `lzma` compression methods. The TarFile class allows reading and writing of TAR archives.

```python
import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames())
```

|Mode|Action|
|:----|:----|
|r|Opens archive for reading with transparent compression|
|r:gz|Opens archive for reading with gzip compression|
|r:bz2|Opens archive for reading with bzip2 compression|
|r:xz|Opens archive for reading with lzma compression|
|w|Opens archive for uncompressed writing|
|w:gz|Opens archive for gzip compressed writing|
|w:xz|Opens archive for lzma compressed writing|
|a|Opens archive for appending with no compression|


Creating new TAR archives and add files to it

```python
>>> import tarfile

>>> file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
>>> with tarfile.open('packages.tar', mode='w') as tar:
...     for file in file_list:
...         tar.add(file)

>>> # Read the contents of the newly created archive
>>> with tarfile.open('package.tar', mode='r') as t:
...     for member in t.getmembers():
...         print(member.name)
```

Making Archives with `shutil`

```python
import shutil

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('data/backup', 'tar', 'data/')
```

Then unpack it...
```python
shutil.unpack_archive('backup.tar', 'extract_dir/')
```