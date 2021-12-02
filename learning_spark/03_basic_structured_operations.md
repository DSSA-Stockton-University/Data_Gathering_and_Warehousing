# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 9

---
# Basic Structured Operations

---

Lets Start with a Dataframe using the example from the book
```python

# This is also found in the Databricks-Datasets directory that can be found using dbutils.fs.ls("/") to explore whats is S3 
df = spark.read.format("json") \
    .load("/mnt/defg/flight-data/json/2015-summary.json")

# Lets look at the schema
df.printSchema()

StructType(
    List(
        StructField(DEST_COUNTRY_NAME, StringType, true),
        StructField(ORIGIN_COUNTRY_NAME, StringType, true),
        StructField(count, LongType, true)
    )
)
```
`StructType` is what makes up a spark schema and is made up of fields called `StructFields` that have a name, type, and boolean flag which specifies whether or not that column can contain missing or null values. 

__Create and enforce a specified schema on a Dataframe__
```python
from pyspark.sql.types import StructField, StructType, StringType

# Defining the Schema to be used
myManualSchema = StructType(
    [
        StructField("DEST_COUNTRY_NAME", StringType(), True),
        StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
        StructField("count", LongType(), False)
    ]
)

# Reading a Dataframe and applying the schema (Schema on Read)
df = spark.read.format("json") \
    .schema(myManualSchema) \
    .load("/mnt/defg/flight-data/json/2015-summary.json")

```

### Working with Columns in a Dataframe__

__Creating a Column__
```python
from pyspark.sql.functions import col, column

# Most commonly used
col("someColumnName")
# Another alias for col
column("someColumnName")
```
__Referring to Columns__
If you need to refer to a column in a Dataframe you can use the `col` method on the dataframe. This is useful when doing operations like _joins_ or _aggregates_

```python
# Creates a new column by adding 10 to a existing df columns called count
df.withColumn('plus10', col('count')+10)
```

__Accessing Dataframe Columns__

```python
spark.read.format("json") \
    .load("/mnt/defg/flight-data/json/2015-summary.json") \
    .columns
```

__Working with Dataframe Rows__
```python
# Gets the first row of the dataframe
df.first()

# Gets the last row of the dataframe
df.last()

from pyspark.sql import Row

# Creating a row 
myRow = Row("Hello", None, 1, False)

# Getting data from a row using its position
myRow[2]
```


### Manipulating DataFrames

```python
# Start off with a DataFrame
df = spark.read.format("json") \
    .load("/mnt/defg/flight-data/json/2015-summary.json")

df.createOrReplaceTempView("dfTable")
```

__Select__ Allows us to work with Columns in a dataFrame

```python
# This is the equivalent of a SQL SELECT Clause
df.select("DEST_COUNTRY_NAME").show(2)

# Selecting multiple columns
df.select(
    "DEST_COUNTRY_NAME",
    "ORGIN_COUNTRY_NAME") \
    .show(2)

# Giving a column an alias
df.select(
    col("DEST_COUNTRY_NAME").alias('country'))
```

__Working with Explicit Values as Literals__

```python
from pyspark.sql.functions import lit

df.select(
    expr("*"),
    lit(1).alias("One")) \
    .show(2)
```

__Adding new Columns__
```python
df.withColumn('newCol', lit(10)).show(2)
```

__Renaming new Columns__
```python
df.withColumnRenamed('oldcol', 'newcol')
```

__Dropping Columns__
```python
df.drop("ORIGIN_COUNTRY_NAME").columns

# Dropping multiple columns
df.drop("ORIGIN_COUNTRY_NAME", "DEST_COUNTRY_NAME")
```

__Changing a Column Datatype__
```python
df.withColumn("count", col("count").cast("int")).printSchema()
```

__Filtering Rows in a DataFrame__
```python
# We can filter a dataframe using .filter or .where
df.where(col("count") < 2) \
    .where(col("ORIGIN_COUNTRY_NAME") != "Croatia") \
    .show(2)

```
__Removing Duplicates__
```python
df.select("ORIGIN_COUNTRY_NAME") \
    .distinct() \
    .count()

```

__Randomly Sampling a DataFrame__
```python
# Create seed for reproducible results
seed = 5

# Do not replace original rows
withReplacement = False

# Fraction of rows to extract from the dataframe
fraction = 0.5

df.sample(withReplacement, fraction, seed).count()
```

__Random Splits__ 
Useful when you need to break up your DataFrame randomly. This is commonly used to create `training`, `validation`, and `test` sets for machine learning algorithms. 

```python
# Split the dataset randomly for test and training sets
test, train = df.randomSplit([0.25, 0.75], seed)
```

__Concatenating Rows__
```python
df.union(newDF) \
    .where("count = 1") \
    .where(col("ORIGIN_COUNTRY_NAME") != "United States") \
    .show()

```

__Sorting Rows__
```python
# Sort ascending by value in the column
df.sort("count").show(5)

# Sort ascending by count then by DEST_COUNTRY_NAME
df.orderBy("count", "DEST_COUNTRY_NAME").show(5)

# Using col expr to do the same as above
df.orderBy(col("count"), col("DEST_COUNTRY_NAME")).show(5)

# descending order and ascending order
from pyspark.sql.functions import desc, asc
df.orderBy(desc(col("count")), asc(col("DEST_COUNTRY_NAME"))).show

# To optimize transformations we can sort partitions beforehand 
spark.read.format("json") \
    .load("/mnt/defg/flight-data/json/*-summary.json") \
    .sortWithinPartitions("count")
```

__Limit the number of rows__
```python
# Limits to 5 rows
df.limit(5).show()

# with sorting
df.orderBy(expr("count desc")).limit(10).show()
```

__Repartition and Coalesce__
Another optimization we can achieve in spark is to partition the data according to columns that are frequently filtered.

Reparition will incur a full shuffle of the data, this means you should typically only repartition when the future number of partitions is greater than your current number of partitions or when you are looking to partition by a set of columns

```python
# Repartitions the dataframe to 5 partitions
df.repartition(5)

```

Coalesce will not incur a full shuffle and tries to combine partitions. This Operations will shuffle data into 5 partitions based on the column. Then coalesce them ()

```python
# Repartitions (with shuffle) to 5 partitions then coalesce to 2 partitions (without shuffle)
df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
```

__Using Collect()__
Collect gets all the data from the entire DataFrames, takes the first N rows, and prints them out. 
```python
collectDF = df.limit(10)
collectDF.take(5) # take works with an Integer count
collectDF.show() # this prints it out nicely
collectDF.show(5, False)
collectDF.collect()
```
