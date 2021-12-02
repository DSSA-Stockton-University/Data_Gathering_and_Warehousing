# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 4

---

## Replication

**Replication** meas keeping a copy of the same data on multiple machines that are connected via a network. 

> Reasons why you might want to replicate data:
> * To keep data geographically close to your users (reducing latency)
> * To allow parts of the system to continue working even if some parts have failed (Increase availability)
> * To scale out the number of machines that can serve read queries (Increase read throughput)

The difficulty in replication lies in handling _changes_ to replicated data. Popular algorithms for replicating changes between nodes: _single-leader_, _multi-leader_, and _leaderless_ replication.

### Leaders and followers

Each *node* that stores a copy of the database is called a _replica_.

Every write to the database needs to be processed by every replica. The most common solution for this is called _leader-based replication_ (_active/passive_).
1. One of the replicas is designated the _leader_ (_master_ or _primary_). Writes to the database must send requests to the leader.
2. Other replicas are known as _followers_ (_read replicas_, _slaves_, _secondaries_ or _hot stanbys_). The leader sends the data change to all of its followers as part of a _replication log_ or _change stream_.
3. Reads can be query the leader or any of the followers, while writes are only accepted on the leader.

![img](/assets/img/replication.png)

**PostgreSQL, MySQL, Oracle Data Guard, SQL Server's AlwaysOn Availability Groups, MongoDB, RethinkDB,  and Espresso** are examples of databases using built-in replication.

**Kafka** and **RabbitMQ** are distributed message brokers that also support it.

#### Synchronous vs asynchronous

**The advantage of synchronous replication** is that the follower is guaranteed to have an up-to-date copy of the data that is consistent with the leader. **The disadvantage** is that it the synchronous follower doesn't respond, the write cannot be processed.**

It's impractical for all followers to be synchronous. If you enable synchronous replication on a database, it usually means that _one_ of the followers is synchronous, and the others are asynchronous. This guarantees up-to-date copy of the data on at least two nodes (this is sometimes called _semi-synchronous_).

Often, leader-based replication is asynchronous. Writes are not guaranteed to be durable, the main advantage of this approach is that the leader can continue processing writes.

![img](/assets/img/leader-based-replication.png)

#### Setting up new followers

Copying data files from one node to another is typically not sufficient.

Setting up a follower can usually be done without downtime. The process looks like this:
1. Take a snapshot of the leader's database
2. Copy the snapshot to the follower node
3. Follower requests data changes that have happened since the snapshot was taken
4. Once follower processed the backlog of data changes since snapshot, it has _caught up_ and can process changes from the leader as they happen.

#### Handling node outages

Any node on the network can go down unexpectedly due to a fault or planned maintenance. 

How is high availability achieved with leader-based replication?

#### Follower Failure: Catchup Recovery
Example: A follower node crashes and is restarted.

Using Catchup Recovery, the follower can connect to the leader and request all the data changes that occurred during the time when the follower was disconnected.


#### Leader Failure: Failover
Example: A leader node crashes and one of the followers needs to be promoted to be the new leader. 

The challenge is that clients will need to be reconfigured to send their writes to the new leader and followers need to start consuming data changes from the new leader.

**Automatic failover consists:**
1. Determining that the leader has failed. If a node does not respond in a period of time it's considered dead.
2. Choosing a new leader. The best candidate for leadership is usually the replica with the most up-to-date changes from the old leader.
3. Reconfiguring the system to use the new leader. The system needs to ensure that the old leader becomes a follower and recognises the new leader.

**Things that could go wrong:**
* If asynchronous replication is used, the new leader may have received conflicting writes.
* Discarding writes is especially dangerous if other storage systems outside of the database need to be coordinated with the database contents.
* It could happen that two nodes both believe that they are the leader (_split brain_). Data is likely to be lost or corrupted.
* What is the right time before the leader is declared dead?

For these reasons, some operation teams prefer to perform failovers manually, even if the software supports automatic failover.

#### Implementation of replication logs

##### Statement-based replication

The leader logs every sql _statement_ and sends it to its followers (every `INSERT`, `UPDATE` or `DELETE`).

This type of replication has some problems:
* Non-deterministic functions such as `NOW()` or `RAND()` will generate different values on replicas.
* Statements that depend on existing data, like auto-increments, must be executed in the same order in each replica.
* Statements that have side effects (e.g. triggers, stored procedures, User-defined functions) may result differently on each replica.

A solution to this is to replace any non-deterministic function with a fixed return value in the leader.

##### Write-ahead log (WAL) shipping

The log is an _append-only_ sequence of bytes containing all writes to the database. The leader can send it to its followers. This way of replication is used in PostgresSQL and Oracle.

The main disadvantage is that the log describes the data at a very low level (like which bytes were changed in which disk blocks), coupling it to the storage engine.

If the database changes it's format from one version to another, it is not typically possible to run different versions of the database in leaders and followers. This can have a big operational impact, like making it impossible to have a zero-downtime upgrade of the database.

##### Logical (row-based) log replication

Basically a sequence of records describing writes to database tables at the granularity of a row:
* For an inserted row, the new values of all columns.
* For a deleted row, the information that uniquely identifies that column.
* For an updated row, the information to uniquely identify that row and all the new values of the columns.

A transaction that modifies several rows, generates several of such logs, followed by a record indicating that the transaction was committed. MySQL binlog uses this approach.

Since logical log is decoupled from the storage engine internals, it's easier to make it backwards compatible.

Logical logs are also easier for external applications to parse, useful for data warehouses, custom indexes and caches (__change data capture__).

##### Trigger-based replication

There are some situations were you may need to move replication up to the application layer.

A trigger lets you register custom application code that is automatically executed when a data change occurs. This is a good opportunity to log this change into a separate table, from which it can be read by an external process.

Main disadvantages is that this approach has greater overheads, is more prone to bugs but it may be useful due to its flexibility.

### Problems with replication lag

Node failures is just one reason for wanting replication. Other reasons are scalability and latency.

In a _read-scaling_ architecture, you can increase the capacity for serving read-only requests simply by adding more followers. However, this only realistically works on asynchronous replication. The more nodes you have, the more likely it is that one will be down.

With an asynchronous approach, a follower may fall behind, leading to inconsistencies in the database (_eventual consistency_).

The _replication lag_ could be a fraction of a second or several seconds or even minutes.

The problems that may arise and how to solve them.

#### Reading your own writes

_Read-after-write consistency_, also known as _read-your-writes consistency_ is a guarantee that if the user reloads the page, they will always see any updates they submitted themselves.

How to implement it:
* **When reading something that the user may have modified, read it from the leader.** For example, user profile information on a social network is normally only editable by the owner. A simple rule is always read the user's own profile from the leader.
* You could track the time of the latest update and, for one minute after the last update, make all reads from the leader.
* The client can remember the timestamp of the most recent write, then the system can ensure that the replica serving any reads for that user reflects updates at least until that timestamp.
* If your replicas are distributed across multiple data centers, then any request needs to be routed to the data center that contains the leader.


Another complication is that the same user is accessing your service from multiple devices, you may want to provide _cross-device_ read-after-write consistency.

Some additional issues to consider:
* Remembering the timestamp of the user's last update becomes more difficult. The metadata will need to be centralized.
* If replicas are distributed across data centers, there is no guarantee that connections from different devices will be routed to the same data center. You may need to route requests from all of a user's devices to the same data center.

![img](/assets/img/rtw.JPG)

#### Monotonic reads

Because of followers can fall behind, it's possible for a user to see things _moving backward in time_.

When you read data, you may see an old value; **monotonic reads** means that if one user makes several reads in sequence, they will not see time go backward.

Make sure that each user always makes their reads from the same replica. The replica can be chosen based on a hash of the user ID. If the replica fails, the user's queries will need to be rerouted to another replica.

![img](/assets/img/mono.JPG)

#### Consistent prefix reads

If a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

This is a particular problem in partitioned (sharded) databases as there is no global ordering of writes.

A solution is to make sure any writes casually related to each other are written to the same partition.

#### Solutions for replication lag

_Transactions_ exist so there is a way for a database to provide stronger guarantees so that the application can be simpler.

### Multi-leader replication

Leader-based replication has one major downside: there is only one leader, and all writes must go through it.

A natural extension is to allow more than one node to accept writes (_multi-leader_, _master-master_ or _active/active_ replication) where each leader simultaneously acts as a follower to the other leaders.

![img](/assets/img/multileader.JPG)

#### Use cases for multi-leader replication

It rarely makes sense to use multi-leader setup within a single data center.

##### Multi-data center operation

* You can have a leader in _each_ data center. 
* Within each data center, regular leader-follower replication is used. 
* Between data centers, each data center leader replicates its changes to the leaders in other data centers.

Compared to a single-leader replication model deployed in multi-data centers
* **Performance.** With single-leader, every write must go across the internet to wherever the leader is, adding significant latency. In multi-leader every write is processed in the local datacenter and replicated asynchronously to other datacenters. The network delay is hidden from users and perceived performance may be better.
* **Tolerance of data center outages.** In single-leader if the data center with the leader fails, failover can promote a follower in another data center. In multi-leader, each data center can continue operating independently from others.
* **Tolerance of network problems.** Single-leader is very sensitive to problems in this inter-data center link as writes are made synchronously over this link. Multi-leader with asynchronous replication can tolerate network problems better.

Multi-leader replication is implemented with:
* Tungsten Replicator for MySQL
* BDR for PostgreSQL
* GoldenGate for Oracle.

##### Clients with offline operation

If you have an application that needs to continue to work while it is disconnected from the internet, every device that has a local database can act as a leader, and there will be some asynchronous multi-leader replication process (imagine, a Calendar application).

CouchDB is designed for this mode of operation.

#### Collaborative editing

_Real-time collaborative editing_ applications allow several people to edit a document simultaneously. Like Etherpad or Google Docs.

The user edits a document, the changes are instantly applied to their local replica and asynchronously replicated to the server and any other user.

If you want to avoid editing conflicts, you must the lock the document before a user can edit it.

For faster collaboration, you may want to make the unit of change very small (like a keystroke) and avoid locking.

#### Handling write conflicts

The biggest problem with multi-leader replication is when conflict resolution is required. This problem does not happen in a single-leader database.

##### Synchronous vs asynchronous conflict detection

In single-leader the second writer can be blocked and wait the first one to complete, forcing the user to retry the write. On multi-leader if both writes are successful, the conflict is only detected asynchronously later in time.

If you want synchronous conflict detection, you might as well use single-leader replication.

##### Conflict avoidance

The simplest strategy for dealing with conflicts is to avoid them. If all writes for a particular record go through the same leader, then conflicts cannot occur.

On an application where a user can edit their own data, you can ensure that requests from a particular user are always routed to the same data center and use the leader in that data center for reading and writing.

##### Converging toward a consistent state

On single-leader, the last write determines the final value of the field.

In multi-leader, it's not clear what the final value should be.

The database must resolve the conflict in a _convergent_ way, all replicas must arrive a the same final value when all changes have been replicated.

Different ways of achieving convergent conflict resolution.
* Five each write a unique ID (timestamp, long random number, UUID, or a has of the key and value), pick the write with the highest ID as the _winner_ and throw away the other writes. This is known as _last write wins_ (LWW) and it is dangerously prone to data loss.
* Give each replica a unique ID, writes that originated at a higher-numbered replica always take precedence. This approach also implies data loss.
* Somehow merge the values together.
* Record the conflict and write application code that resolves it a to some later time (perhaps prompting the user).

##### Custom conflict resolution

Multi-leader replication tools let you write conflict resolution logic using application code.

* **On write.** As soon as the database system detects a conflict in the log of replicated changes, it calls the conflict handler.
* **On read.** All the conflicting writes are stored. On read, multiple versions of the data are returned to the application. The application may prompt the user or automatically resolve the conflict. CouchDB works this way.

#### Multi-leader replication topologies

A _replication topology_ describes the communication paths along which writes are propagated from one node to another.

The most general topology is _all-to-all_ in which every leader sends its writes to every other leader. MySQL uses _circular topology_, where each nodes receives writes from one node and forwards those writes to another node. Another popular topology has the shape of a _star_, one designated node forwards writes to all of the other nodes.

In circular and star topologies a write might need to pass through multiple nodes before they reach all replicas. To prevent infinite replication loops each node is given a unique identifier and the replication log tags each write with the identifiers of the nodes it has passed through. When a node fails it can interrupt the flow of replication messages.

In all-to-all topology fault tolerance is better as messages can travel along different paths avoiding a single point of failure. It has some issues too, some network links may be faster than others and some replication messages may "overtake" others. To order events correctly. there is a technique called _version vectors_. PostgresSQL BDR does not provide casual ordering of writes, and Tungsten Replicator for MySQL doesn't even try to detect conflicts.

### Leaderless replication

Simply put, any replica can directly accept writes from clients. Databases like look like Amazon's in-house _Dynamo_ datastore. _Riak_, _Cassandra_ and _Voldemort_ follow the _Dynamo style_.

In a leaderless configuration, failover does not exist. Clients send the write to all replicas in parallel.

_Read requests are also sent to several nodes in parallel_. The client may get different responses. Version numbers are used to determine which value is newer.

Eventually, all the data is copied to every replica. After a unavailable node come back online, it has two different mechanisms to catch up:
* **Read repair.** When a client detect any stale responses, write the newer value back to that replica.
* **Anti-entropy process.** There is a background process that constantly looks for differences in data between replicas and copies any missing data from one replica to he other. It does not copy writes in any particular order.

#### Quorums for reading and writing

If there are _n_ replicas, every write must be confirmed by _w_ nodes to be considered successful, and we must query at least _r_ nodes for each read. As long as _w_ + _r_ > _n_, we expect to get an up-to-date value when reading. _r_ and _w_ values are called _quorum_ reads and writes. Are the minimum number of votes required for the read or write to be valid.

A common choice is to make _n_ and odd number (typically 3 or 5) and to set _w_ = _r_ = (_n_ + 1)/2 (rounded up).

Limitations:
* Sloppy quorum, the _w_ writes may end up on different nodes than the _r_ reads, so there is no longer a guaranteed overlap.
* If two writes occur concurrently, and is not clear which one happened first, the only safe solution is to merge them. Writes can be lost due to clock skew.
* If a write happens concurrently with a read, the write may be reflected on only some of the replicas.
* If a write succeeded on some replicas but failed on others, it is not rolled back on the replicas where it succeeded. Reads may or may not return the value from that write.
* If a node carrying a new value fails, and its data is restored from a replica carrying an old value, the number of replicas storing the new value may break the quorum condition.

**Dynamo-style databases are generally optimised for use cases that can tolerate eventual consistency.**

#### Sloppy quorums and hinted handoff

Leaderless replication may be appealing for use cases that require high availability and low latency, and that can tolerate occasional stale reads.

It's likely that the client won't be able to connect to _some_ database nodes during a network interruption.
* Is it better to return errors to all requests for which we cannot reach quorum of _w_ or _r_ nodes?
* Or should we accept writes anyway, and write them to some nodes that are reachable but aren't among the _n_ nodes on which the value usually lives?

The latter is known as _sloppy quorum_: writes and reads still require _w_ and _r_ successful responses, but those may include nodes that are not among the designated _n_ "home" nodes for a value.

Once the network interruption is fixed, any writes are sent to the appropriate "home" nodes (_hinted handoff_).

Sloppy quorums are useful for increasing write availability: as long as any _w_ nodes are available, the database can accept writes. This also means that you cannot be sure to read the latest value for a key, because it may have been temporarily written to some nodes outside of _n_.

##### Multi-datacenter operation

Each write from a client is sent to all replicas, regardless of datacenter, but the client usually only waits for acknowledgement from a quorum of nodes within its local datacenter so that it is unaffected by delays and interruptions on cross-datacenter link.

#### Detecting concurrent writes

In order to become eventually consistent, the replicas should converge toward the same value. If you want to avoid losing data, you application developer, need to know a lot about the internals of your database's conflict handling.

* **Last write wins (discarding concurrent writes).** Even though the writes don' have a natural ordering, we can force an arbitrary order on them. We can attach a timestamp to each write and pick the most recent. There are some situations such caching on which lost writes are acceptable. If losing data is not acceptable, LWW is a poor choice for conflict resolution.
* **The "happens-before" relationship and concurrency.** Whether one operation happens before another operation is the key to defining what concurrency means. **We can simply say that to operations are _concurrent_ if neither happens before the other.** Either A happened before B, or B happened before A, or A and B are concurrent.

##### Capturing the happens-before relationship

The server can determine whether two operations are concurrent by looking at the version numbers.
* The server maintains a version number for every key, increments the version number every time that key is written, and stores the new version number along the value written.
* Client reads a key, the server returns all values that have not been overwrite, as well as the latest version number. A client must read a key before writing.
* Client writes a key, it must include the version number from the prior read, and it must merge together all values that it received in the prior read.
* Server receives a write with a particular version number, it can overwrite all values with that version number or below, but it must keep all values with a higher version number.

##### Merging concurrently written values

No data is silently dropped. It requires clients do some extra work, they have to clean up afterward by merging the concurrently written values. Riak calls these concurrent values _siblings_.

Merging sibling values is the same problem as conflict resolution in multi-leader replication. A simple approach is to just pick one of the values on a version number or timestamp (last write wins). You may need to do something more intelligent in application code to avoid losing data.

If you want to allow people to _remove_ things, union of siblings may not yield the right result. An item cannot simply be deleted from the database when it is removed, the system must leave a marker with an appropriate version number to indicate that the item has been removed when merging siblings (_tombstone_).

Merging siblings in application code is complex and error-prone, there are efforts to design data structures that can perform this merging automatically (CRDTs).

#### Version vectors

We need a version number _per replica_ as well as per key. Each replica increments its own version number when processing a write, and also keeps track of the version numbers it has seen from each of the other replicas.

The collection of version numbers from all the replicas is called a _version vector_.

Version vector are sent from the database replicas to clients when values are read, and need to be sent back to the database when a value is subsequently written. Riak calls this _casual context_. Version vectors allow the database to distinguish between overwrites and concurrent writes.

---
## Partitioning

Replication, for very large datasets or very high query throughput is not sufficient, we need to break the data up into _partitions_ (_sharding_).

Basically, each partition is a small database of its own.

The main reason for wanting to partition data is _scalability_, query load can be distributed across many processors. Throughput can be scaled by adding more nodes.


### Partitioning and replication

Each record belongs to exactly one partition, it may still be stored on several nodes for fault tolerance.

A node may store more than one partition.

![img](/assets/img/partition.JPG)

### Partition of key-value data

**Which distribution of partitioned data gives the best performance results?**
![img](/assets/img/CommonDistributions.png)


Our goal with partitioning is to spread the data and the query load evenly across nodes.

If partition is unfair, we call it _skewed_. It makes partitioning much less effective. A partition with disproportionately high load is called a _hot spot_.

The simplest approach is to assign records to nodes randomly. The main disadvantage is that if you are trying to read a particular item, you have no way of knowing which node it is on, so you have to query all nodes in parallel.

![img](/assets/img/skew.png)

#### Partition by key range

* Assigns a continuous range of keys, like the volumes of a paper encyclopedia.
* Boundaries might be chose manually by an administrator, or the database can choose them automatically. 
* On each partition, keys are in sorted order so scans are easy.

The downside is that certain access patterns can lead to skew.

![img](/assets/img/keyrange.JPG)

#### Partitioning by hash of key

A good hash function takes skewed data and makes it uniformly distributed. There is no need to be cryptographically strong (MongoDB uses MD5 and Cassandra uses Murmur3). You can assign each partition a range of hashes. The boundaries can be evenly spaced or they can be chosen pseudo-randomly (_consistent hashing_).

Unfortunately we lose the ability to do efficient range queries. Keys that were once adjacent are now scattered across all the partitions. Any range query has to be sent to all partitions.

![img](/assets/img/hashpart.JPG)

#### Skewed workloads and relieving hot spots

You can't avoid hot spots entirely. For example, you may end up with large volume of writes to the same key.

It's the responsibility of the application to reduce the skew. A simple technique is to add a random number to the beginning or end of the key.

Splitting writes across different keys, makes reads now have to do some extra work and combine them.

### Partitioning and secondary indexes

The situation gets more complicated if secondary indexes are involved. A secondary index usually doesn't identify the record uniquely. They don't map neatly to partitions.

#### Partitioning secondary indexes by document

Each partition maintains its secondary indexes, covering only the documents in that partition (_local index_).

You need to send the query to _all_ partitions, and combine all the results you get back (_scatter/gather_). This is prone to tail latency amplification and is widely used in MongoDB, Riak, Cassandra, Elasticsearch, SolrCloud and VoltDB.

#### Partitioning secondary indexes by term

We construct a _global index_ that covers data in all partitions. The global index must also be partitioned so it doesn't become the bottleneck.

It is called the _term-partitioned_ because the term we're looking for determines the partition of the index.

Partitioning by term can be useful for range scans, whereas partitioning on a hash of the term gives a more even distribution load.

The advantage is that it can make reads more efficient: rather than doing scatter/gather over all partitions, a client only needs to make a request to the partition containing the term that it wants. The downside of a global index is that writes are slower and complicated.

### Re-balancing partitions

The process of moving load from one node in the cluster to another.

Strategies for re-balancing:
* **How not to do it: Hash mod n.** The problem with _mod N_ is that if the number of nodes _N_ changes, most of the keys will need to be moved from one node to another.
* **Fixed number of partitions.** Create many more partitions than there are nodes and assign several partitions to each node. If a node is added to the cluster, we can _steal_ a few partitions from every existing node until partitions are fairly distributed once again. The number of partitions does not change, nor does the assignment of keys to partitions. The only thing that change is the assignment of partitions to nodes. This is used in Riak, Elasticsearch, Couchbase, and Voldemort. **You need to choose a high enough number of partitions to accomodate future growth.** Neither too big or too small.
* **Dynamic partitioning.** The number of partitions adapts to the total data volume. An empty database starts with an empty partition. While the dataset is small, all writes have to processed by a single node while the others nodes sit idle. HBase and MongoDB allow an initial set of partitions to be configured (_pre-splitting_).
* **Partitioning proportionally to nodes.** Cassandra and Ketama make the number of partitions proportional to the number of nodes. Have a fixed number of partitions _per node_. This approach also keeps the size of each partition fairly stable.

#### Automatic versus manual re-balancing

Fully automated re-balancing may seem convenient but the process can overload the network or the nodes and harm the performance of other requests while the re-balancing is in progress.

It can be good to have a human in the loop for re-balancing. You may avoid operational surprises.

### Request routing

This problem is also called _service discovery_. There are different approaches:
1. Allow clients to contact any node and make them handle the request directly, or forward the request to the appropriate node.
2. Send all requests from clients to a routing tier first that acts as a partition-aware load balancer.
3. Make clients aware of the partitioning and the assignment of partitions to nodes.

In many cases the problem is: **how does the component making the routing decision learn about changes in the assignment of partitions to nodes?**

Many distributed data systems rely on a separate coordination service such as ZooKeeper to keep track of this cluster metadata. Each node registers itself in ZooKeeper, and ZooKeeper maintains the authoritative mapping of partitions to nodes. The routing tier or the partitioning-aware client, can subscribe to this information in ZooKeeper. HBase, SolrCloud and Kafka use ZooKeeper to track partition assignment. MongoDB relies on its own _config server_. Cassandra and Riak take a different approach: they use a _gossip protocol_.

#### Parallel query execution

__Massively parallel processing__ (MPP) relational database products are much more sophisticated in the types of queries they support.

* The MPP query optimizer breaks a complex query into a number of execution stages and partitions which can be executed in parallel.
* Queries that involve scanning over large parts
of the dataset particularly benefit from parallel execution.
* Fast parallel execution of data warehouse queries is a specialized topic, and given the
business importance of analytics, it gets a lot of commercial interest. 