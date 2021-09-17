# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 2

---
![img](/assets/img/database.png)

---
## Reliable, scalable, and maintainable applications
A data-intensive application is typically built from standard building blocks. They usually need to:
* Store data (_databases_)
* Speed up reads (_caches_)
* Search data (_search indexes_)
* Send a message to another process asynchronously (_stream processing_)
* Periodically crunch data (_batch processing_)

A data-intensive application also must be designed for:
* **Reliability** - To work _correctly_ even in the face of _adversity_.
* **Scalability** - Reasonable ways of dealing with growth.
* **Maintainability** - Be able to work on it _productively_.

---
### Reliability

Typical expectations:
* Application behaves and functions as the performs the function the user expected
* Tolerate the user making mistakes
* Its performance is good
* The system prevents abuse

Systems that anticipate faults and can cope with them are called _fault-tolerant_ or _resilient_.

**A fault is usually defined as one component of the system deviating from its spec**, whereas _failure_ is when the system as a whole stops providing the required service to the user.

You should generally **prefer tolerating faults over preventing faults**.

* **Hardware faults** - Until recently, redundancy of hardware components was sufficient for most applications. As data volumes increase, more applications use a larger number of machines, proportionally increasing the rate of hardware faults. **There is a move towards systems that tolerate the loss of entire machines**. A system that tolerates machine failure can be patched one node at a time, without downtime of the entire system (_rolling upgrade_).

* **Software errors** - It is unlikely that a large number of hardware components will fail at the same time. Software errors are a systematic error within the system, they tend to cause many more system failures than uncorrelated hardware faults.

* **Human errors** - Humans are known to be unreliable. Configuration errors by operators are a leading cause of outages. You can make systems more reliable:
    1. Minimizing the opportunities for error
        - For example: designing interfaces that make easy to do the "right thing" and discourage the "wrong thing".
    2. Provide fully featured non-production _sandbox_ environments where people can explore and experiment safely.
        - **Note**: Data Scientist typically work within sandboxes to develop their models or analyses. 
    3. Automated testing 
    4. Quick and easy recovery from human error, fast to rollback configuration changes, roll out new code gradually and tools to recompute data.
    5. Set up detailed and clear monitoring, such as performance metrics and error rates (_telemetry_).
    6. Implement good management practices and training.

### Scalability

Scalability tells us how we should cope with increased load. In order to understand how to scale, we need to clearly describe the current load on the system. Only then we can discuss growth questions.

---

#### Twitter example

Twitter main operations
- Post tweet: a user can publish a new message to their followers (Avg. 4.6k req/sec, with over 12k req/sec at peak)
- Home timeline: a user can view tweets posted by the people they follow (300k req/sec)

Two ways of implementing those operations:
1. Posting a tweet simply inserts the new tweet into a global collection of tweets. When a user requests their home timeline, look up all the people they follow, find all the tweets for those users, and merge them (sorted by time). This could be done with a SQL `JOIN`.
2. Maintain a cache for each user's home timeline. When a user _posts a tweet_, look up all the people who follow that user, and insert the new tweet into each of their home timeline caches.

Approach 1, systems struggle to keep up with the load of home timeline queries. So the company switched to approach 2. The average rate of published tweets is almost two orders of magnitude lower than the rate of home timeline reads.

Downside of approach 2 is that posting a tweet now requires a lot of extra work. Some users have over 30 million followers. A single tweet may result in over 30 million writes to home timelines.

Twitter moved to an hybrid of both approaches. Tweets continue to be fanned out to home timelines but a small number of users with a very large number of followers are fetched separately and merged with that user's home timeline when it is read, like in approach 1.

---

#### Describing performance
Once you have described the load on your system, you can investigate what happens when load increases.

>What happens when the load increases:
>* When you increase a load parameter and keep system resources unchanged, how is the performance affected?
>* When you increase a load parameter, how much do you need to increase your resources?

In a batch processing system such as Hadoop, we usually care about _throughput_, or the number of records we can process per second.

In an online system, the _response_ time of a service is usually more important (time spent sending a request and receiving a response).

> ##### Latency and response time
> The response time is what the client sees. 
> Latency is the duration that a request is waiting to be handled.

It's common to see the _average_ response time of a service reported. However, the mean is not very good metric if you want to know your "typical" response time, it does not tell you how many users actually experienced that delay.
![img](/assets/img/response_time.png)
**Better to use percentiles.**
* _Median_ (_50th percentile_ or _p50_). Half of user requests are served in less than the median response time, and the other half take longer than the median
* Percentiles _95th_, _99th_ and _99.9th_ (_p95_, _p99_ and _p999_) are good to figure out how bad your outliners are.

**Service level objectives** (SLOs) and **service level agreements** (SLAs) are contracts that define the expected performance and availability of a service.

>An SLA may state the median response time to be less than 200ms and a 99th percentile under 1s. **These metrics set expectations for clients of the service and allow customers to demand a refund if the SLA is not met.**

Queueing delays often account for large part of the response times at high percentiles. **It is important to measure times on the client side.**

When generating load artificially, the client needs to keep sending requests independently of the response time.

> ##### Percentiles in practice
> ![img](/assets/img/parallel.png)
> High percentiles become especially important in backend services that are called multiple times to serve a single end-user request. 
> - The end-user request still needs to wait for the slowest of the parallel calls to complete.
> - The chance of getting a slow call increases if an end-user request requires multiple backend calls.

#### Approaches for coping with load

* _Scaling up_ or _vertical scaling_: Moving to a more powerful machine
* _Scaling out_ or _horizontal scaling_: Distributing the load across multiple smaller machines.
* _Elastic_ systems: Automatically add computing resources when detected load increase. Quite useful if load is unpredictable.

> A system that is designed to handle 100K req/sec, each 1kB in size, looks very different from a system designed to handle 3 req/sec, each 2GB in size - even though the two systems have the same data throughput.

An architecture that scales **is built around which operations will be common and which will be rare (the load parameters**

### Maintainability

The majority of software cost is ongoing maintenance. There are three design principles for software systems:
* **Operability** - Make it easy for operation teams to keep the system running.
* **Simplicity** - Easy for new engineers to understand the system by removing as much complexity as possible.
* **Evolvability** - Make it easy for engineers to make changes to the system in the future.

#### Operability: making life easy for operations

A good operations team is responsible for
* Monitoring and quickly restoring service if it goes into a undesired state
* Tracking down the cause of problems
* Keeping software and platforms up to date
* Keeping tabs on how different systems affect each other
* Anticipating future problems
* Establishing good practices and development tools
* Perform complex maintenance tasks, like platform migration
* Maintaining the security of the system
* Defining processes that make operations predictable
* Preserving the organization's knowledge about the system

**Good operability means making routine tasks easy.**

#### Simplicity: managing complexity

When complexity makes maintenance hard, budget and schedules are often overrun. There is a greater risk of introducing bugs.

Making a system simpler means removing _accidental_ complexity, as non inherent in the problem that the software solves (as seen by users).

One of the best tools we have for removing accidental complexity is _abstraction_ that hides the implementation details behind clean and simple to understand APIs and facades.

#### Evolvability: making change easy

_Agile_ working patterns provide a framework for adapting to change.

---
#### Wrapping Up
Applications have to meet various requirements in order to be useful:
* _Functional requirements_: tell us what the application should do
* _Nonfunctional requirements_: tell us what general properties like security, reliability, compliance, scalability, compatibility and maintainability an application should have

---
