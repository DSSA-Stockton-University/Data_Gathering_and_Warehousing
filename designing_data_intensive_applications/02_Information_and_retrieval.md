# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 3

---
# Storage and Retrieval

Databases need to do two things: Store the data and give the data back to you.

### Data structures that power up your database

Many databases use a _log_, which is append-only data file. Databases need to be designed to deal with things like _concurrency control_ and _reclaiming disk space_ so the log doesn't grow forever and handling errors and partially written records).

> A __log__ is an append-only sequence of records

In order to efficiently find the value for a particular key, we need a different data structure: an _index_. An **index** is an _additional_ structure that is derived from the primary data.

> Well-chosen indexes <u>speed up read queries</u> but every index added will <u>slows down writes</u>. That's why databases don't index everything by default, but require you to choose indexes manually using your knowledge on typical query patterns.

#### Hash indexes
Key-value stores are quite similar to the _dictionary_ type (hash map or hash table).

Let's say our storage consists only of appending to a file. The simplest indexing strategy is to keep an in-memory hash map where every key is mapped to a byte offset in the data file. Whenever you append a new key-value pair to the file, you also update the hash map to reflect the offset of the data you just wrote. The only requirement this type of database has has is that:
1. All the keys fit in the available RAM.
2. Values can use more space than there is available in memory, since they can be loaded from disk.

**Byte-offset** - is the number of character that exists counting from the beginning of a line.

![img](/assets/img/hashindex.jfif)

The storage engine becomes well suited for situations where the value of each key is updated frequently and it's feasible to keep all keys in memory.

As we only ever append to a file, so how do we avoid eventually running out of disk space? 
> **Break the log into segments of certain size by closing the segment file when it reaches a certain size, and making subsequent writes to a new segment file. We can then perform _compaction_ on these segments.** 

**Compaction** means throwing away duplicate keys in the log, and keeping only the most recent update for each key.

> - We can also merge several segments together at the same time as performing the compaction. 
> - Segments are never modified after they have been written, so the merged segment is written to a new file.
> - Merging and compaction of frozen segments can be done in a background thread. After the merging process is complete, we switch read requests to use the new merged segment instead of the old segments, and the old segment files can simply be deleted.

Each segment now has its own in-memory hash table, mapping keys to file offsets. In order to find a value for a key, we first check the most recent segment hash map; if the key is not present we check the second-most recent segment and so on. The merging process keeps the number of segments small, so lookups don't need to check many hash maps.

Some issues that are important in a real implementation:
* **File format** - It is simpler to use `binary` format.
* **Deleting records** - Append special deletion record to the data file (_tombstone_) that tells the merging process to discard previous values.
* **Crash recovery** - If restarted, the in-memory hash maps are lost. You can recover from reading each segment but that would take long time. You can speed up recovery by storing a snapshot of each segment hash map on disk.
* **Partially written records** - The database may crash at any time. A `checksums` allowing corrupted parts of the log to be detected and ignored.
* **Concurrency control** - As writes are appended to the log in a strictly sequential order, a common implementation is to have a single writer thread. Segments are immutable, so they can be read concurrently by multiple threads.

 Append-only design turns out to be good for several reasons:
* **Appending and segment merging** are sequential write operations, much faster than random writes, especially on magnetic spinning-disks.
* **Concurrency and crash recovery** are much simpler.
* **Merging old segments** avoids files getting fragmented over time.

Hash table has its limitations too:
* **Hash table must fit in memory** - It is difficult to make an on-disk hash map perform well.
* **Range queries** are not efficient.

---
#### SSTables and LSM-Trees

We introduce a new requirement to segment (log) files: we require that **the sequence of key-value pairs is _sorted by key_**.

**_Sorted String Table_, or _SSTable_** - requires that each key only appears once within each merged segment file (compaction already ensures that). 

> SSTables have few big advantages over log segments with hash indexes
>1. **Merging segments is simple and efficient** (we can use algorithms like _mergesort_). When multiple segments contain the same key, we can keep the value from the most recent segment and discard the values in older segments.
>2. **You no longer need to keep an index of all the keys in memory.** For a key like `handiwork`, when you know the offsets for the keys `handback` and `handsome`, you know `handiwork` must appear between those two. You can jump to the offset for `handback` and scan from there until you find `handiwork`, if not, the key is not present. You still need an in-memory index to tell you the offsets for some of the keys. One key for every few kilobytes of segment file is sufficient.
>3. Since read requests need to scan over several key-value pairs in the requested range anyway, **it is possible to group those records into a block and compress it** before writing it to disk.

How do we get the data sorted in the first place? With red-black trees or AVL trees, you can insert keys in any order and read them back in sorted order.
* When a write comes in, add it to an in-memory balanced tree structure similar  (_memtable_).
> A **balanced tree**, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
* When the memtable gets bigger than some threshold (megabytes), write it out to disk as an SSTable file. Writes can continue to a new memtable instance.
* On a read request, try to find the key in the memtable, then in the most recent on-disk segment, then in the next-older segment, etc.
* From time to time, run merging and compaction in the background to discard overwritten and deleted values.

![img](/assets/img/memtbl.webp)

If the database crashes, the most recent writes are lost. We can keep a separate log on disk to which every write is immediately appended. That log is not in sorted order, but that doesn't matter, because its only purpose is to restore the memtable after crash. Every time the memtable is written out to an SSTable, the log can be discarded.

**Storage engines that are based on this principle of merging and compacting sorted files are often called LSM structure engines (Log Structure Merge-Tree).**

Lucene, an indexing engine for full-text search used by **Elasticsearch** and Solr, uses a similar method for storing its _term dictionary_.

There are also different strategies to determine the order and timing of how SSTables are compacted and merged. Mainly two _size-tiered_ and _leveled_ compaction. LevelDB and RocksDB use leveled compaction, HBase use size-tiered, and Cassandra supports both. In size-tiered compaction, newer and smaller SSTables are successively merged into older and larger SSTables. In leveled compaction, the key range is split up into smaller SSTables and older data is moved into separate "levels", which allows the compaction to use less disk space.

---

#### B-trees

This is the most widely used indexing structure. **B-tress** keep key-value pairs sorted by key, which allows efficient key-value lookups and range queries.

>Comparing Log-structures vs B-trees:
> * The log-structured indexes break the database down into variable-size _segments_ (megabytes).
>
> * B-trees break the database down into fixed-size _blocks_ or _pages_, traditionally 4KB.

One page is designated as the _root_ and you start from there. The page contains several keys and references to child pages.

If you want to update the value for an existing key in a B-tree:
* Search for the leaf page containing that key
* change the value in that page
* write the page back to disk. 

If you want to add new key:
* find the correct page then add it to the page. 
>If there isn't enough free space in the page to accommodate the new key, it is split in two half-full pages, and the parent page is updated to account for the new subdivision of key ranges.

Writing operations of B-Trees:
* The basic underlying write operation is to overwrite a page on disk with new data. 
> It is assumed that the overwrite does not change the location of the page, all references to that page remain intact. This is a big contrast to log-structured indexes such as LSM-trees, which only append to files.

#### Comparing B-trees and LSM-trees

* LSM-trees are typically faster for writes, whereas B-trees are thought to be faster for reads.
* Reads are typically slower on LSM-tress as they have to check several different data structures and SSTables at different stages of compaction.

Advantages of LSM-trees:
* LSM-trees are typically able to sustain higher write throughput (the amount of data) than B-trees, party because they sometimes have lower write amplification: a write to the database results in multiple writes to disk. The more a storage engine writes to disk, the fewer writes per second it can handle.
* LSM-trees can be compressed better, and thus often produce smaller files on disk than B-trees. Where  B-trees tend to leave disk space unused due to fragmentation.

Downsides of LSM-trees:
* Compaction process can sometimes interfere with the performance of ongoing reads and writes. B-trees can be more predictable. The bigger the database, the the more disk bandwidth is required for compaction. Compaction cannot keep up with the rate of incoming writes, if not configured properly you can run out of disk space.
* On B-trees, each key exists in exactly one place in the index. This offers strong transactional semantics. Transaction isolation is implemented using locks on ranges of keys, and in a B-tree index, those locks can be directly attached to the tree.

#### Other indexing structures

We've only discussed key-value indexes, which are like _primary key_ index. There are also _secondary indexes_.

A secondary index can be easily constructed from a key-value index. The main difference is that in a secondary index, the indexed values are not necessarily unique. There are two ways of doing this: making each value in the index a list of matching row identifiers or by making a each entry unique by appending a row identifier to it.

#### Full-text search and fuzzy indexes

Indexes don't allow you to search for _similar_ keys, such as misspelled words. Such _fuzzy_ querying requires different techniques.

Full-text search engines allow synonyms, grammatical variations, occurrences of words near each other.

Lucene uses SSTable-like structure for its term dictionary. Lucene, the in-memory index is a finite state automaton, similar to a _trie_.

#### Keeping everything in memory

Disks have two significant advantages: they are durable, and they have lower cost per gigabyte than RAM.

It's quite feasible to keep them entirely in memory, this has lead to _in-memory_ databases.

Some **in-memory databases** aim for durability (like Redis), with special hardware, writing a log of changes to disk, writing periodic snapshots to disk or by replicating in-memory sate to other machines.

> * When an in-memory database is restarted, it needs to reload its state, either from disk or over the network from a replica. 
>
> * The disk is merely used as an append-only log for durability, and reads are served entirely from memory.

Products such as VoltDB, MemSQL, and Oracle TimesTime are in-memory databases. Redis and Couchbase provide weak durability.

**In-memory databases can be faster because they can avoid the overheads of encoding in-memory data structures into a form that can be written to disk**.


---
### Transaction processing or analytics?

A _transaction_ is a group of reads and writes that form a logical unit, this pattern became known as _online transaction processing_ (OLTP).

_Data analytics_ has very different access patterns. A query would need to scan over a huge number of records, only reading a few columns per record, and calculates aggregate statistics.

These queries are often written by business analysts, and fed into reports. This pattern became known for _online analytics processing_ (OLAP).

![img](/assets/img/oltp_olap.png)

#### Data warehousing

A _data warehouse_ is a separate database that analysts can query to their heart's content without affecting OLTP operations. It contains read-only copy of the dat in all various OLTP systems in the company. Data is extracted out of OLTP databases (through periodic data dump or a continuous stream of update), transformed into an analysis-friendly schema, cleaned up, and then loaded into the data warehouse (process _Extract-Transform-Load_ or ETL).

A data warehouse is most commonly relational, but the internals of the systems can look quite different.

**Amazon RedShift** is hosted version of ParAccel. Apache Hive, Spark SQL, Cloudera Impala, Facebook Presto, Apache Tajo, and Apache Drill. Some of them are based on ideas from Google's Dremel.

Data warehouses are used in fairly formulaic style known as a **_star schema_**.

**Facts** are captured as individual events, because this allows maximum flexibility of analysis later. The fact table can become extremely large.

**Dimensions** represent the _who_, _what_, _where_, _when_, _how_ and _why_ of the event.

The name "star schema" comes from the fact than when the table relationships are visualised, the fact table is in the middle, surrounded by its dimension tables, like the rays of a star.

![img](/assets/img/starschema.jpg)

* Fact tables can be huge and sometimes contain over several hundred. 
* Dimension tables can also be very wide.

### Column-oriented storage

In a row-oriented storage engine, when you do a query that filters on a specific field, the engine will load all those rows with all their fields into memory, parse them and filter out the ones that don't meet the requirement. This can take a long time.

_Column-oriented storage_ is simple: don't store all the values from one row together, but store all values from each _column_ together instead. If each column is stored in a separate file, a query only needs to read and parse those columns that are used in a query, which can save a lot of work.

Column-oriented storage often lends itself very well to compression as the sequences of values for each column look quite repetitive, which is a good sign for compression. A technique that is particularly effective in data warehouses is _bitmap encoding_.

Bitmap indexes are well suited for all kinds of queries that are common in a data warehouse.

> Cassandra and HBase have a concept of _column families_, which they inherited from Bigtable.

Besides reducing the volume of data that needs to be loaded from disk, column-oriented storage layouts are also good for making efficient use of CPU cycles (_vectorized processing_).

**Column-oriented storage, compression, and sorting helps to make read queries faster** and make sense in data warehouses, where most of the load consist on large read-only queries run by analysts. The downside is that writes are more difficult.

An update-in-place approach, like B-tree use, is not possible with compressed columns. If you insert a row in the middle of a sorted table, you would most likely have to rewrite all column files.

When the underlying data changes, a materialized view needs to be updated, because it is denormalized copy of the data. Database can do it automatically, but writes would become more expensive.

![img](/assets/img/normalized-vs-denormalized.png)

A common special case of a materialized view is know as a _data cube_ or _OLAP cube_, a grid of aggregates grouped by different dimensions.

![img](/assets/img/cube.jfif)