# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 2
**Week**: 9

---
# Introduction to Apache Spark

---

## What is Apache Spark

__Apache Spark__ is a distributed data processing system written in scala for working with large datasets. Spark consist of _Spark Core_ and a growing ecosystem of tools, libraries and languages. 

Spark supports the following Programming Languages:
* R (SparkR)
* Scala
* SQL
* Python (Pyspark)

Spark supports a variety of analytic libraries for network analysis, machine learning, and MLOps:
* MLlib (Spark machine learning library)
* MLFlow (MLOps for ML Operationalization)
* GraphX for processing large graphs


### What is Spark's Architecture?
Spark is a distributed architecture that utilizes _clusters_.

__Clusters__ refers to a group of machines that can be can manage and coordinated workloads by pooling resources together.

__Spark Application__ refers to a spark program that consist of a _driver_ and set of _workers_ called executors. 

__Driver__ node is responsible for:
1. Maintaining information about the Spark App
2. Responding to the user's program
3. Scheduling and distributing work across the worker nodes

__Executors__ are responsible for:
1. Executing the code assigned to it by the driver
2. Reporting the state of the computation to the driver

__Cluster Manager__ controls the physical machines and allocates resources to the Spark App. Spark's default cluster manager uses __YARN__, __Mesos__, or __Kubernetes__ (which is a newer development)

__Local Mode__ allows you to run spark apps on your individual computer instead of a cluster. This is useful for development and debugging spark apps. 

Diagram of Spark App Architecture
![img](/assets/img/Apache-Spark-architecture.png)


To Start Spark from the terminal
```bash
# Start a Spark shell
./bin/spark-shell

# Start Pyspark
./bin/pyspark
```

### What is the Spark Session

__Spark Session__ is used to manifest the driver process. The _SparkSession_ is the entry point for executing spark code. In Pyspark, the `SparkSession` is an object that is assigned to the variable `spark`. In Databricks, a default session is created without having to initialize one. 

Example of a SparkSession 
```python
# Notice we can set spark configs and name our spark app!
SparkSession.builder \
    .master("local") \
    .appName("Stockton") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```

### What are Spark DataFrames?

A __Spark DataFrame__ is a table of data with rows and columns. The list of columns and their data types are called a _schema_.  Spark DataFrames are spread across multiple executors on the cluster. The reason for putting the data on more than one computer is to:
- Process data that is too large to fit on one machine
- Reduce Latency to perform computation on one machine

__Other Data Abstractions in Spark__ 
- Datasets
- SQL Tables
- Resilient Distributed Datasets (RDDS)

### How is Data Processed on a Spark Cluster

In order to process data on the cluster, Spark breaks up data into _partitions_. Where one or more partitions are kept on an executor. Spark will operate on each partition in parallel unless the operation calls for a _shuffle_. 

A __shuffle__ occurs when an operation needs to share data multiple partitions in parallel. In Spark, Dataframes give us the ability to work and manipulate partitions.

__Transformations__ are instructions that tell spark how to modify a dataframe. Transformations in spark are lazily evaluated.

__Lazy Evaluation__ means Spark will wait to execute your transformations. Instead, it makes an efficient plan to determine the best way to execute across the cluster. we can access this plan using the `.explain()` method with our dataframes

__Actions__ trigger spark to compute results from your transformations. 


### Spark UI
Contains information about the state of Spark Jobs, Environment, and Cluster State. It is useful for tuning and debugging.

__TempView__ gives us another way to perform operations against Dataframes using SQL. Using the method:

```python
# Creating a SQL Interface for a Dataframe
df.createOrReplaceTempView('temp_table') 

# Using Spark SQL
sqlWay = spark.sql("""
SELECT DEST_COUNTRY_NAME, count(1)
FROM temp_table
GROUP BY DEST_COUNTRY_NAME
""")

# Same transformations using Pyspark
dataFrameWay = df \
    .groupBy("DEST_COUNTRY_NAME")\
    .count()

# View plans for both methods
sqlWay.explain()
dataFrameWay.explain()
``` 

More Complex Example using Multi-transformations
```python
from pyspark.sql.functions import desc

# The below spark transformations do a groupBy on Country Name
# Sum to count the total destination flights.
# Rename to change the agg columns header
# Sort to sort the results from greatest to least 
# limit the result to 5 rows and collect to return the data to the user 
flightData2015 \
    .groupBy("DEST_COUNTRY_NAME") \
    .sum("count") \
    .withColumnRenamed("sum(count)", "destination_total")\
    .sort(desc("destination_total")) \
    .limit(5) \
    .collect()
```

