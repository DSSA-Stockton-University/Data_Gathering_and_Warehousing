# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 6

---
![img](/assets/img/sleep.jfif)

---

## Data Encoding & Processing

Data often comes in all kinds of common encodings, such as `CSV`, `JSON`, `XML`, and `Databases`. The main problem for data encoding and processing is knowing how to get data in and out of a program.

#### Working with CSV Files
For most kinds of CSV data, use the `csv` library in python. For example, suppose you have some
stock market data in a file named stocks.csv like this:
```
 Symbol,Price,Date,Time,Change,Volume
 "AA",39.48,"6/11/2007","9:36am",-0.18,181800
 "AIG",71.38,"6/11/2007","9:36am",-0.15,195500
 "AXP",62.58,"6/11/2007","9:36am",-0.46,935000
 "BA",98.31,"6/11/2007","9:36am",+0.12,104800
 "C",53.08,"6/11/2007","9:36am",-0.25,360900
 "CAT",78.29,"6/11/2007","9:36am",-0.23,225400
```

```python
# use the csv library to work with csv files
import csv

# still use open() for I/O
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)
```


Here each `row` will be a `tuple` where you will need
to use indexing, such as row[0] and row[4] to access certain fields.


Alternatively, we can read the data as a sequence of dictionaries instead. 
```python
import csv
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
    # process row
```

Additionally, we can use the library called `pandas`. 

__pandas__ is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for Python. It is also the de-facto data wrangling tool of data scientist and engineers.  

In pandas...
```python
import pandas as pd

df = pd.read_csv('stocks.csv')
```
To write CSV data, you also use the csv module but create a writer object. For example:
```python
import csv

# Create a list of file headers 
headers = ['Symbol','Price','Date','Time','Change','Volume']

# Create a list of tuples containing our data
rows = [
    ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 19550),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000]
with open('stocks.csv','w') as f:
    f_csv = csv.writer(f)
    # Remember to write the headers first
    f_csv.writerow(headers)
    f_csv.writerows(rows)
```
Writing a csv file if our data is stored as python dicts
```python
import csv

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    {'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
    {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
    {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
 'Time':'9:36am', 'Change':-0.46, 'Volume': 935000}]
with open('stocks.csv','w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

```

In pandas, our data is represented as a dataframe so writing csv files is easy...
```python
import pandas as pd

# Pass a data structure to the DataFrame constructor class
df = pd.DataFrame(...)

# use the to_csv method to write the dataframe to a csv file
df.to_csv('stock.csv')
```

#### Working with JSON files

What is JSON?
* JSON stands for JavaScript Object Notation and is an open standard data-interchange format. 
* JSON is lightweight and self-describing making it easy to read and write. 
* JSON is language independent.
* JSON supports data structures such as arrays and objects.

You want to read or write data encoded as JSON in python. The `json` module provides an easy way to encode and decode data in JSON. 

The two main functions are `json.dumps()` and `json.loads()`, mirroring the interface used in
other serialization libraries, such as `pickle`. 

Here is how you turn a Python data structure into JSON:
```python
import json
# its easy to convert data to json when its already a dict

# In-memory data structure
data = {
 'name' : 'ACME',
 'shares' : 100,
 'price' : 542.23
}
json_str = json.dumps(data)
```
Here is how you turn a JSON-encoded string back into a Python data structure:
```python
data = json.loads(json_str)
```

If you are working with files instead of strings, you can alternatively use `json.dump()`
and `json.load()` to encode and decode JSON data. For example:
```python
# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)
# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)
```
Normally, JSON decoding will create `dicts` or `lists` from the supplied data. If you want to create different kinds of objects, supply the `object_pairs_hook` or `object_hook` to `json.loads()`. 

Here is how you would decode JSON data, preserving its
order in an OrderedDict:
```python
from collections import OrderedDict

# A json string
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

# using the object_pairs_hook argument of json.loads()
data = json.loads(s, object_pairs_hook=OrderedDict)
data
```
output
```
OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)]
```

Reading Json strings in pandas
```python
import json

some_json_string = ...
s = json.loads(some_json_string) #gives us the json object as lists and dicts

pd.read_json(s)
```
```
        date         B         A
0 2013-01-01  2.565646 -1.206412
1 2013-01-01  1.340309  1.431256
2 2013-01-01 -0.226169 -1.170299
3 2013-01-01  0.813850  0.410835
4 2013-01-01 -0.827317  0.132003
```
Or reading JSON from a file in pandas
```python
pd.read_json("test.json")

#gives us this
                   A         B       date  ints  bools
2013-01-01 -1.294524  0.413738 2013-01-01     0   True
2013-01-02  0.276662 -0.472035 2013-01-01     1   True
2013-01-03 -0.013960 -0.362543 2013-01-01     2   True
2013-01-04 -0.006154 -0.923061 2013-01-01     3   True
2013-01-05  0.895717  0.805244 2013-01-01     4   True
```
We can also convert Dataframes back to JSON strings
```python
df = pd.DataFrame(
    dict(A=range(1, 4), B=range(4, 7), C=range(7, 10)),
    columns=list("ABC"),
    index=list("xyz"),
)
```
looks like this
```
   A  B  C
x  1  4  7
y  2  5  8
z  3  6  9
```
convert back to JSON string
```python
df.to_json(orient="columns")
# gives us this
'{"A":{"x":1,"y":2,"z":3},"B":{"x":4,"y":5,"z":6},"C":{"x":7,"y":8,"z":9}}'
```


#### Working with relational databases

Sometimes you may need to insert, update or delete rows from a database. Remember that rows of a database are just `tuples`, therefore we can easily mock a database table in python by the following:

```python
stocks = [
 ('GOOG', 100, 490.1),
 ('AAPL', 50, 545.75),
 ('FB', 150, 7.45),
 ('HPQ', 75, 33.2),
]

```
Given data in this form, it is relatively straightforward to interact with a relational
database using Python’s standard database API called `sqlite3`. The API allows us to perform operations on the database as SQL queries. 

__Note__: different database (e.g., MySql, Postgres, or ODBC), you’ll have to install separate packages like `SQLAlchemy`

The first step is to connect to the database. Typically, you execute a connect() function, supplying parameters such as the name of the database, hostname, username, password, and other details as needed. 

Connection example:
```python
import sqlite3
db = sqlite3.connect('database.db')
```
To do anything with the data, you next create a cursor. Once you have a cursor, you can start executing SQL queries. 

Cursor example:
```python
# creates a cursor object
c = db.cursor()

# executes sql query
c.execute('create table portfolio (symbol text, shares integer, price real)')
<sqlite3.Cursor object at 0x10067a730>

# sends the commit statement back to the database
db.commit()
```


To insert a sequence of rows into the data, use a statement like this:
```python
stocks = [
 ('GOOG', 100, 490.1),
 ('AAPL', 50, 545.75),
 ('FB', 150, 7.45),
 ('HPQ', 75, 33.2),
]

# All rows become part of the transaction
c.executemany('insert into portfolio values (?,?,?)', stocks)
<sqlite3.Cursor object at 0x10067a730>

db.commit()
```

Reading from the database uses a statement like this:
```python
for row in db.execute('select * from portfolio'):
    print(row)
```
each row is returned as a tuple like this:
```python
('GOOG', 100, 490.1)
('AAPL', 50, 545.75)
('FB', 150, 7.45)
('HPQ', 75, 33.2)
```

#### Summarizing data and performing statistics
Lets say we need to crunch through large datasets and generate summaries or other kinds of statistics.

The pandas library is really the defacto standard for any kind of data analysis involving statistics, time series, and other related techniques

Lets analyze the City of Chicago rat and rodent database, which consist of a a CSV file with about 74,000 rows:
```python
import pandas
# Read a CSV file, skipping last line
rats = pandas.read_csv('rats.csv', skip_footer=1)

# Gives us the DataFrame object with all the columns
<class 'pandas.core.frame.DataFrame'>
Int64Index: 74055 entries, 0 to 74054
Data columns:
Creation Date 74055 non-null values
Status 74055 non-null values
Completion Date 72154 non-null values
Service Request Number 74055 non-null values
Type of Service Request 74055 non-null values
Number of Premises Baited 65804 non-null values
Number of Premises with Garbage 65600 non-null values
Number of Premises with Rats 65752 non-null values
Current Activity 66041 non-null values
Most Recent Action 66023 non-null values
Street Address 74055 non-null values
ZIP Code 73584 non-null values
X Coordinate 74043 non-null values
Y Coordinate 74043 non-null values
Ward 74044 non-null values
Police District 74044 non-null values
Community Area 74044 non-null values
Latitude 74043 non-null values
Longitude 74043 non-null values
Location 74043 non-null values
dtypes: float64(11), object(9)

# Investigate range of values for a certain field
rats['Current Activity'].unique()
```
```python
# Gives us an array of all the unique values for that column
array([nan, Dispatch Crew, Request Sanitation Inspector], dtype=object)
```
```python
# Filter the data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
len(crew_dispatched)
65676

# Find 10 most rat-infested ZIP codes in Chicago
crew_dispatched['ZIP Code'].value_counts()[:10]
60647 3837 # Lots of rats here
60618 3530
60614 3284
60629 3251
60636 2801
60657 2465
60641 2238
60609 2206
60651 2152
60632 2071

# Group by completion date
dates = crew_dispatched.groupby('Completion Date')
<pandas.core.groupby.DataFrameGroupBy object at 0x10d0a2a10>
len(dates)
472

# Determine counts on each day
date_counts = dates.size()
date_counts[0:10]
Completion Date
01/03/2011 4
01/03/2012 125
01/04/2011 54
01/04/2012 38
01/05/2011 78
01/05/2012 100
01/06/2011 100
01/06/2012 58
01/07/2011 1
01/09/2012 12

# Sort the counts
date_counts.sort()
date_counts[-10:]
Completion Date
10/12/2012 313
10/21/2011 314
09/20/2011 316
10/26/2011 319
02/22/2011 325
10/26/2012 333
03/17/2011 336
10/13/2011 378
10/14/2011 391
10/07/2011 457 # very busy day for rats

