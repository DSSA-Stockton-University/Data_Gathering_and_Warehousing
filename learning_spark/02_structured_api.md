# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 9

---
# Apache Spark Structured APIs

---

### What is the Structured APIs?

__Structured vs Unstructured data__:
* Structured Data (and semi-structured) refer to data that has structure a computer can understand easily. 

* Unstructured Data refers to data much harder to a computer (images, text, audio, video)

__Structured API__ provide us the ability to make transformations on structured and semi-structured data using DataFrames, Datasets, and Spark SQL. The Structured APIs provide fundamental abstraction to write data flows for big data. There are two main types of operations:
- Batch
- Streaming


__Schema__ defines the column names and data types of a DataFrame. Users can define schemas manually or infer them in Spark. This process is called _schema on read_ because the schema is not applied to the data until after it is read. Spark has its own schema that is different from Scala and Python Data Types. 

```python
# Simple df consisting of a range of numbers
df = spark.range(500).toDF("number")
df.select(df["number"] + 10)
# DataFrame[(number + 10): bigint]
```
Spark Data Types can be accessed using pyspark moduleL
```python
from pyspark.sql.types import *
# Byte Type
b = byteType()

```

### Overview of Spark Execution
1. Write Transformation for DataFrames, Datasets or SQL
2. If code is valid, Spark converts code to a _Logical Plan_
3. Spark Converts the Logical Plan into a Physical Plan
4. Spark executed the Physical plan on the cluster

>"To execute code, we have to write code. This code is then submitted to Spark either through the console or via a submitted job. This code then passes through the Catalyst Optimizer which decides how the code should be executed and lays out a plan for doing so, before  finally the code is run and the result is
returned to the user"


![img](/assets/img/catalyst.JPG)

### Logical Plan
Designed to take user code and covert it to a plan. The logical plan represents a set of abstract transformation that do not refer to executors or drivers, but is purely to convert the users expressions into the most optimized version.

__Unresolved Logical Plan__ is the logical plan that converts your code. It considered unresolved because it only checks the syntax of your code and not if tables or columns exist. 

__Catalog__ is a repository of all tables and Dataframe information. 

__Analyzer__ reviews and may reject unresolved logical plans if it requires a table or column that does not exist in the Catalog. 

__Optimizer__ represents the collection of rules that are used to optimize the logical plan.

![img](/assets/img/logical.JPG)

### Physical Plan

__Physical Plans__ specifies how the logical plan will execute on the cluster by generating physical execution strategies and comparing them through a cost model. Physical planning results in a series of RDDs and transformations. Spark takes queries in DataFrames, Datasets, and SQL and compiles them into RDD Transformations automatically. 

![img](/assets/img/pysical.JPG)

### Execution
Spark will select an optimal physical plan, and run all of the code over RDDs. Spark performs further optimizations at runtime by generating native Java Byte code that can remove whole tasks or stages during execution and return the result to the user. 