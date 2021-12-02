# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 10

---
# Working with Different Types of Data

---
Note: The functions module is part of the `pyspark` libraries instead of `org.apache.spark` which is used in scala
 
Spark Data Types:
* Booleans
* Numbers
* Strings
* Dates and Timestamps
* Handling Nulls
* Complex Types
* User Defined Functions (UDF)

Starting off with a Spark DataFrame

```python
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/mnt/defg/retail-data/by-day/2010-12-01.csv")

df.printSchema()
df.createOrReplaceTempView("dfTable")
```

##### Using Booleans

```python
from pyspark.sql.functions import col

# where is also an alias for filter
df.where(col("InvoiceNo") != 536365) \
    .select("InvoiceNo", "Description") \
    .show(5, False)

# The above expression determined what rows to filter using a python conditional
```
```python
from pyspark.sql.functions import instr

priceFilter = col("UnitPrice") > 600
descripFilter = instr(df.Description, "POSTAGE") >= 1

# Using a boolean filter with the or operator in python
df.where(df.StockCode.isin("DOT"))\
    .where(priceFilter | descripFilter)\
    .show(5)
```

##### Using Numbers

```python
from pyspark.sql.functions import expr, pow

fabricatedQuantity = pow(col("Quantity") * col("UnitPrice"), 2)
df.select(expr("CustomerId"), fabricatedQuantity.alias("realQuantity"))\
    .show(2)
```

__Rounding Numbers in spark__
```python
from pyspark.sql.functions import lit, round, bround

# Round will round up between two numbers where bround will round down
df.select(
    round(lit("2.5")),
    bround(lit("2.5")))\
    .show(2)
```

__Pearson Correlation__
```python
from pyspark.sql.functions import corr

# We can use the corr method to get the pearson correlation between two columns
df.stat.corr("Quantity", "UnitPrice")
df.select(corr("Quantity", "UnitPrice")).show()

```
##### Working with Text

```python
from pyspark.sql.functions import lower, upper

# using upper and lower to make text uppercase or lowercase
df.select(
    col("Description"),
    lower(col("Description")),
    upper(lower(col("Description")))) \
    .show(2)

```

__Removing whitespace around text__
```python
from pyspark.sql.functions import lit, ltrim, rtrim, rpad, lpad

df.select(
    ltrim(lit(" HELLO ")).alias("ltrim"),
    rtrim(lit(" HELLO ")).alias("rtrim"),
    trim(lit(" HELLO ")).alias("trim"),
    lpad(lit("HELLO"), 3, " ").alias("lp"),
    rpad(lit("HELLO"), 10, " ").alias("rp"))\
    .show(2)
```

__Regular Expressions__
```python
from pyspark.sql.functions import regexp_replace

regex_string = "BLACK|WHITE|RED|GREEN|BLUE"

df.select(
    regexp_replace(col("Description"), regex_string, "COLOR")
    .alias("color_cleaned"),
    col("Description"))\
    .show(2)

```

__Character Replacement at the index using `translate`__
```python
from pyspark.sql.functions import translate

# Will replace
df.select(
    translate(col("Description"), "LEET", "1337"),
    col("Description"))\
    .show(2)
```
__Checking if text exists and return a boolean using `instr`__

```python
from pyspark.sql.functions import instr

containsBlack = instr(col("Description"), "BLACK") >= 1
containsWhite = instr(col("Description"), "WHITE") >= 1

df.withColumn("hasSimpleColor", containsBlack | containsWhite)\
    .filter("hasSimpleColor")\
    .select("Description")\
    .show(3, False)

```

##### Working with Dates

```python
from pyspark.sql.functions import current_date, current_timestamp

# get the current date & timestamp 
dateDF = spark.range(10)\
    .withColumn("today", current_date())\
    .withColumn("now", current_timestamp())

dateDF.createOrReplaceTempView("dateTable")
dateDF.printSchema()
```

__Add or Subtract days from a date__
```python
from pyspark.sql.functions import date_add, date_sub

dateDF \
    .select(
    date_sub(col("today"), 5),
    date_add(col("today"), 5)) \
    .show(1)

```

__Getting the Days or Months between two dates__

```python
from pyspark.sql.functions import datediff, months_between, to_date

# Get the number of days between two dates by using datediff
dateDF\
    .withColumn("week_ago", date_sub(col("today"), 7))\
    .select(datediff(col("week_ago"), col("today")))\
    .show(1)

# Get the number of months between two dates using months_between
dateDF\
    .select(
    to_date(lit("2016-01-01")).alias("start"),
    to_date(lit("2017-05-22")).alias("end"))\
    .select(months_between(col("start"), col("end")))\
    .show(1)

```

__Convert a string to a date in spark__
```python

from pyspark.sql.functions import to_date, lit

spark.range(5).withColumn("date", lit("2017-01-01"))\
    .select(to_date(col("date")))\
    .show(1)

```