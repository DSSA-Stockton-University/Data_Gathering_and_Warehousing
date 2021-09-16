# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 2

---
## Data Models and Query Language

Most applications are built by layering one data model on top of another. Each layer hides the complexity of the layers below by providing a clean data model. These abstractions allow different groups of people to work effectively.

### Relational Model vs Document Model

The roots of relational databases lie in _business data processing_, which was performed on mainframe computers in the 1960s and 70s. Today, relational databases are heavily relied on for _transaction processing_ (entering sales or bank transactions) and _batch processing_ (reporting, analytics, payroll, invoicing).


> Many competitors to the relational models have come and gone over the years:
> -    Network model
> -    Hierarchical model
> -    XML Databases

#### NoSQL Databases
Since 2010, distributed non-relational databases have become increasingly popular and open-sourced.
> _Not Only SQL_ or _NoSQL_ has a few driving forces:
>* Greater scalability
>* preference for free and open source software
>* Specialized query optimizations
>* Desire for a more dynamic and expressive data model

#### Object-relational Mismatch
Most application development is done in object-oriented programming languages, which leads to criticism of the SQL data model: 
> With a SQL model, if data is stored in a relational tables, an awkward translation layer is required between the objects in the application code and the database model of tables rows and columns. **This disconnect between models is called _impedance mismatch_.**

Object-relational mapping (ORM) frameworks reduce the amount of boilerplate code required for this translation layer, but they can't completely hide the differences between the two models. 

>In python, SQLAlchemy is one of the most popular ORMs
>![img](/assets/img/orm-examples.png)


#### Document-Oriented Databases

Document-oriented databases like MongoDB try to reduce impedance mismatch between the application code and storage layer. The lack of schema is often cited as an advantage for _JSON Models_.

JSON representation has better _locality_ than the multi-table SQL schema. All the relevant information is in one place, and one query is sufficient.  Whereas in a relational model, you often need to perform multiple queries and joins to retrieve all the relevant information. 

![img](/assets/img/nosql.png)

- In relational databases, it's normal to refer to rows in other tables by ID, because joins are easy. 
- In document databases, joins are not needed for one-to-many tree structures, and support for joins is often weak.

>If the database itself does not support joins, you have to emulate a join in application code by making multiple queries.

**The main arguments in favour of the document data model are schema flexibility, better performance due to locality, and sometimes closer data structures to the ones used by the applications. The relation model counters by providing better support for joins, and many-to-one and many-to-many relationships.**

---

#### The Network Model

Standardized by a committee called the Conference on Data Systems Languages (CODASYL) model was a generalization of the hierarchical model. 
- In the tree structure of the **hierarchical model**, every record has exactly one parent
- In the **network model**, a record could have multiple parents.

The links between records are like pointers in a programming language. The only way of accessing a record was to follow a path from a root record called _access path_.

A **pointer** is nothing but a memory location where data is stored.

A query in CODASYL was performed by moving a _cursor_ through the database by iterating over a list of records. If you didn't have a path to the data you wanted, you were in a difficult situation as it was difficult to make changes to an application's data model.

A database **cursor** can be thought of as a pointer to a specific row within a query result. The pointer can be moved from one row to the next. 

![img](/assets/img/networkdb.jpg)

---

#### The Relational Model

The relational model was a way to lay out all the data in the open" a relation (table) is simply a collection of tuples (rows), and that's it.

The query optimizer automatically decides which parts of the query to execute in which order, and which indexes to use (the access path).

The relational model thus made it much easier to add new features to applications.

![img](/assets/img/relational.png)
---

#### Which Data Model Should I Use?

If the data in your application has a document-like structure, then it's probably a good idea to use a document model. The relational technique of _shredding_ can lead unnecessary complicated application code.

The poor support for joins in document databases may or may not be a problem.

If you application does use many-to-many relationships, the document model becomes less appealing. Joins can be emulated in application code by making multiple requests. Using the document model can lead to significantly more complex application code and worse performance.

**Recap of Relationships**
![img](/assets/img/relationships.jpg)
#### Schema flexibility

Most document databases do not enforce any schema on the data in documents. Arbitrary keys and values can be added to a document, when reading, **clients have no guarantees as to what fields the documents may contain.**

Document databases are sometimes called _schemaless_, but maybe a more appropriate term is _schema-on-read_, in contrast to _schema-on-write_.

Schema-on-read is similar to dynamic (runtime) type checking, whereas schema-on-write is similar to static (compile-time) type checking.

Use the schema-on-read approach if the items on the collection don't have all the same structure (heterogeneous)
* Many different types of objects
* Data determined by external systems


#### Data locality for queries

If your application often needs to access the entire document, there is a performance advantage to this _storage locality_.

The database typically needs to load the entire document, even if you access only a small portion of it. On updates, the entire document usually needs to be rewritten, it is recommended that you keep documents fairly small.

### Convergence of Document and Relational databases

PostgreSQL does support JSON documents. RethinkDB supports relational-like joins in its query language and some MongoDB drivers automatically resolve database references. Relational and document databases are becoming more similar over time.

### Query languages for data

In an _imperative language_, you must tell the computer to perform certain operations in order. By contrast, SQL is a _declarative_ query language.

In a **declarative query language** you just specify the pattern of the data you want, but not _how_ to achieve that goal.

A declarative query language hides implementation details of the database engine, making it possible for the database system to introduce performance improvements without requiring any changes to queries.

Declarative languages often lend themselves to parallel execution while imperative code is very hard to parallelize across multiple cores because it specifies instructions that must be performed in a particular order. Declarative languages specify only the pattern of the results, not the algorithm that is used to determine results.

#### Declarative queries on the web

In a web browser, using declarative CSS styling is much better than manipulating styles imperatively in JavaScript. Declarative languages like SQL turned out to be much better than imperative query APIs.

#### MapReduce querying

_MapReduce_ is a programming model for processing large amounts of data in bulk across many machines, popularized by Google.

Mongo offers a MapReduce solution.

```js
db.observations.mapReduce(
    function map() { 2
        var year  = this.observationTimestamp.getFullYear();
        var month = this.observationTimestamp.getMonth() + 1;
        emit(year + "-" + month, this.numAnimals); 3
    },
    function reduce(key, values) { 4
        return Array.sum(values); 5
    },
    {
        query: { family: "Sharks" }, 1
        out: "monthlySharkReport" 6
    }
);
```

The `map` and `reduce` functions must be _pure_ functions, they cannot perform additional database queries and they must not have any side effects. These restrictions allow the database to run the functions anywhere, in any order, and rerun them on failure.

A usability problem with MapReduce is that you have to write two carefully coordinated functions. A declarative language offers more opportunities for a query optimizer to improve the performance of a query. For there reasons, MongoDB 2.2 added support for a declarative query language called _aggregation pipeline_

```js
db.observations.aggregate([
    { $match: { family: "Sharks" } },
    { $group: {
        _id: {
            year:  { $year:  "$observationTimestamp" },
            month: { $month: "$observationTimestamp" }
        },
        totalAnimals: { $sum: "$numAnimals" }
    } }
]);
```

### Graph-like data models

If many-to-many relationships are very common in your application, it becomes more natural to start modelling your data as a graph.

A graph consists of _vertices_ (_nodes_ or _entities_) and _edges_ (_relationships_ or _arcs_).

Well-known algorithms can operate on these graphs, like the shortest path between two points, or popularity of a web page.

There are several ways of structuring and querying the data. The _property graph_ model (implemented by Neo4j, Titan, and Infinite Graph) and the _triple-store_ model (implemented by Datomic, AllegroGraph, and others). There are also three declarative query languages for graphs: Cypher, SPARQL, and Datalog.

![img](/assets/img/graphdb.png)

#### Property graphs

Each vertex (Node) consists of:
* Unique identifier
* Outgoing edges
* Incoming edges
* Collection of properties (key-value pairs)

Each edge consists of:
* Unique identifier
* Vertex at which the edge starts (_tail vertex_)
* Vertex at which the edge ends (_head vertex_)
* Label to describe the kind of relationship between the two vertices
* A collection of properties (key-value pairs)

Graphs provide a great deal of flexibility for data modelling. Graphs are good for evolvability.

---

* _Cypher_ is a declarative language for property graphs created by Neo4j
* Graph queries in SQL. In a relational database, you usually know in advance which joins you need in your query. In a graph query, the number if joins is not fixed in advance. In Cypher `:WITHIN*0...` expresses "follow a `WITHIN` edge, zero or more times" (like the `*` operator in a regular expression). This idea of variable-length traversal paths in a query can be expressed using something called _recursive common table expressions_ (the `WITH RECURSIVE` syntax).

---

#### Triple-stores and SPARQL

In a triple-store, all information is stored in the form of very simple three-part statements: _subject_, _predicate_, _object_ (peg: _Jim_, _likes_, _bananas_). A triple is equivalent to a vertex in graph.

#### The SPARQL query language

_SPARQL_ is a query language for triple-stores using the RDF data model.

#### The foundation: Datalog

_Datalog_ provides the foundation that later query languages build upon. Its model is similar to the triple-store model, generalized a bit. Instead of writing a triple (_subject_, _predicate_, _object_), we write as _predicate(subject, object)_.

We define _rules_ that tell the database about new predicates and rules can refer to other rules, just like functions can call other functions or recursively call themselves.

Rules can be combined and reused in different queries. It's less convenient for simple one-off queries, but it can cope better if your data is complex.