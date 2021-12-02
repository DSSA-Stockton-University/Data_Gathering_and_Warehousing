# DSSA Data Gathering & Warehousing

**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 3
**Week**: 12

---
## Deploying Fast Scalable APIs with FastAPI

![img](/assets/img/fastapi.png)

---

### What is FastAPI?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:
* __Fast__: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
* __Fast to code__: Increase the speed to develop features by about 200% to 300%.
* __Fewer bugs__: Reduce about 40% of human (developer) induced errors.
* __Intuitive__: Great editor support. Completion everywhere. Less time debugging.
* __Easy__: Designed to be easy to use and learn. Less time reading docs.
* __Short__: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* __Robust__: Get production-ready code. With automatic interactive documentation.
* __Standards-based__: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

### Using FastAPI
#### Basic FastAPI Example
1. Create a new virtual environment using `conda` or `pipenv`
    * Using `Pipenv`
        ```python
        # Create your virtual enviroment with Pipenv
        pipenv --python 3.8
        # Access Pipenv Virtual Environment
        pipenv shell
        ```
    * Using `Conda`
        ```python
        # Using Conda to create your virtual environment
        conda create -n <your_environment_name> python=3.8
        # Accessing Conda Virtual Environment
        conda activate <your_environment_name>
        ```
1. Install the `requirements.txt` file
    ```python
    # using pip
    pip install -r requirements.txt
    
    # using pipenv
    pipenv install -r requirements.txt
    
    # using conda
    conda install --file requirements.txt
    ```
1. Create a `main.py` file
    * Linux
        ```bash
        touch main.py
        ```
    * Windows
        ```bash
        echo > main.py
        ```
1. add the following lines of code
    * using an synchronous example
        ```python
        from typing import Optional
        from fastapi import FastAPI
        
        app = FastAPI()
        
        @app.get("/")
        def read_root():
            return {"Hello": "World"}
        
        
        @app.get("/items/{item_id}")
        def read_item(item_id: int, q: Optional[str] = None):
            return {"item_id": item_id, "q": q}
        
        ```
    * Or using an asynchronous example `main.py`:
        ```python
        
        from typing import Optional
        from fastapi import FastAPI
        
        app = FastAPI()
        
        
        @app.get("/")
        async def read_root():
            return {"Hello": "World"}
        
        @app.get("/items/{item_id}")
        async def read_item(item_id: int, q: Optional[str] = None):
            return {"item_id": item_id, "q": q}
        ```
5. Run the server in the terminal
    ```bash
    uvicorn main:app --reload
    ```
    Lets break down the command `uvicorn main:app` refers to:
    - __main__: the file `main.py` (the Python "module").
    - __app__: the object created inside of `main.py` with the line `app = FastAPI()`.
    - __--reload__: make the server restart after code changes. Only do this for development and remember to remove this when running in production.

6. In your web browser, enter `http://localhost:8000/items/5?q=some_query`
    * This URL is actually invoking our `get_item()` function using `5` as the input to the `item_id` argument and `some_query` as the input to `q`, which is an optional string argument 
7. Next Lets look at our API documentation that is automatically generated using __Swagger__ or __Redoc__
    * http://127.0.0.1:8000/docs - See more about [Swagger](https://github.com/swagger-api/swagger-ui)
    * http://127.0.0.1:8000/redoc - See more about [redoc](https://github.com/Redocly/redoc)

__Now lets enhance our basic example to include `PUT` request by replacing our `main.py` with the following code:
```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# New 
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# New
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price,"item_id": item_id}
```
Since Uvicorn is running with `--reload` the server should reload after you've made changes to the `main.py`

__Note__: A "path" is also commonly called an "endpoint" or a "route".

---

## Type Hints (Revisited)

We already know that Python has support for optional "type hints". In case you, you forgot "type hints" are a special syntax that allow declaring the type of a variable.

By declaring types for your variables, editors and tools can give you better support.

FastAPI is all based on these type hints, they give it many advantages and benefits. 

### Declaring types¶
The main place to declare type hints is using function arguments. This is also the main place you would use them with FastAPI.

#### Simple types
You can declare all the standard Python types:
* `int`
* `float`
* `str`
* `bool`
* `bytes`

#### Generic types
There are some data structures that can contain other values, like `dict`, `list`, `set` and `tuple`. These data structures internal values can have their own type too.

To declare those types and the internal types, you can use the standard Python module `typing`. It exists specifically to support these type hints.

For example, let's define a variable to be a list of str.
```python
from typing import List

# remember to use a colon for setting type hints
def process_items(items: List[str]):
    for item in items:
        print(item)
```
This means the argument items is a list, and each of the items elements is a str. By doing this the editor can provide support for items while processing the list. 

Lets look at an example using a Set, Tuple & Dict
```python
from typing import Set, Tuple, Dict

# using set or tuple
def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s

# using dict
def process_things(prices: Dict[str, float]):
    for thing_name, thing_price in prices.items():
        print(thing_name)
        print(thing_price)
```

Example using Optional Arguments with Type hints
```python
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

```
Using `Optional[str]` instead of just `str` will let the editor help you detecting errors where you could be assuming that a value is always a `str`, when it could actually be `None` too.

#### Class Types
```python
class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

```
__Note__: To access autocompletion in vscode use `ctrl + space`

--- 

#### Pydantic

__Pydantic__ a Python library to perform data validation.

You declare the "shape" of the data as python classes containing attributes, where each attribute has a type.

Then you create an instance of that class with some values and it will validate the values, convert them to the appropriate type (if that's the case) and give you an object with all the data.

And you get all the editor support with that resulting object.
Taken from the official Pydantic docs:

```python
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "John Doe" # Notice this is a default value
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123

```
What's going on here:

__`id`__ is using type `int` - The annotation-only declaration tells pydantic that this field is required. `Strings`, `bytes` or `floats` will be coerced to `int` if possible, otherwise an exception will be raised.

__`name`__ is inferred as a `str` from the provided default,  because it has a default, it is not required.

__`signup_ts`__ is a `datetime` field which is not required (and takes the value `None` if it's not supplied) - pydantic will process either a unix timestamp int (e.g. 1496498400) or a string representing the date & time.

__`friends`__ uses python's typing system, and requires a list of `int` - As with id, integer-like objects will be converted to `int`. If validation fails pydantic will raise an error with a breakdown of what was wrong:

### Path Operations

#### Creating Path Opertaions
While building an API, the "path" is the main way to separate "concerns" and "resources". 

__Path__ - refers to the last part of the URL starting from the first `/`. 

So, in a URL like: `https://example.com/items/foo`
...the path would be: `/items/foo`

__Operation__ here refers to one of the HTTP "methods":
* POST
* GET
* PUT
* DELETE
* OPTIONS
* HEAD
* PATCH
* TRACE
In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

When building APIs, you normally use these specific HTTP methods to perform a specific action. Normally you use:
* __POST__: to create data.
* __GET__: to read data.
* __PUT__: to update data.
* __DELETE__: to delete data.
So, in OpenAPI, each of the HTTP methods is called an "operation".

#### Define a path operation decorator

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

```
The `@app.get("/")` tells FastAPI that the function right below is in charge of handling requests that go to:
* the path `/` 
* using a `get` operation

Other path operation decorators:
You can also use the other operations:
* `@app.post()`
* `@app.put()`
* `@app.delete()`
* `@app.options()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`

#### Define a path operation function

What is "path operation function":
* _path_ is `/`
* _operation_ is `get`
* __function__ is the function below the "decorator" (i.e. below `@app.get("/")`).

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
This is a Python function.

It will be called by FastAPI whenever it receives a request to the URL __"/"__ using a __GET__ operation.

In this case, it is an async function. You can also return a `dict`, `list`, singular values as `str`, `int`, etc.

You can also return Pydantic models (you'll see more about that later).

There are many other objects and models that will be automatically converted to JSON (including ORMs, etc). Try using your favorite ones, it's highly probable that they are already supported.

### Summary
1. `Import FastAPI`.
1. Create an `app` instance.
1. Write a path operation decorator (like `@app.get("/")`).
1. Write a path operation function (like `def root(): ...`).
1. Run the development server (like `uvicorn main:app --reload`).