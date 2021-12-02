# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 3
**Week**: 11

---
# Concurrency in Python

![img](/assets/img/funny.png)

---

### What is Concurrency?

__Concurrency__ is when two tasks overlap in execution. With concurrent programming, the performance of our applications and software systems can be improved because we can concurrently deal with the requests rather than waiting for a previous one to be completed.

Concurrency allows tasks to overlap in execution. It could be a situation where:
1. An application is progressing one or more task at the same time 
2. Multiple tasks are making progress at the same time.

Example of Multiple Tasks running concurrently
![img](/assets/img/concurrency.jpg)

__Levels of Concurrency__

* __Low-Level Concurrency__ - uses explicit atomic operations. We cannot use such kind of concurrency for application building, as it is very error-prone and difficult to debug. Even Python does not support such kind of concurrency.

* __Mid-Level Concurrency__ - In this concurrency, there is no use of explicit atomic operations. It uses the explicit locks. Python and other programming languages support such kind of concurrency. Mostly application programmers use this concurrency.

* __High-Level Concurrency__ - In this concurrency, neither explicit atomic operations nor explicit locks are used. Python has `concurrent.futures` module to support such kind of concurrency.

__Properties of Concurrent Systems__
For a program or concurrent system to be correct, some properties must be satisfied by it. Properties related to the termination of system are as follows:
* __Correctness property__ - means that the program or the system must provide the desired correct answer. To keep it simple, we can say that the system must map the starting program state to final state correctly.

* __Safety property__ - means that the program or the system must remain in a “good” or “safe” state and never does anything “bad”.

* __Liveness property__ - means that a program or system must “make progress” and it would reach at some desirable state.

### What is Multi-Threading?
__Thread__ is the smallest unit of execution that can be performed in an operating system. Threads are not independent of one other, instead each thread shares code section, data section, etc. with other threads. They are also known as lightweight processes.

>A thread consists of the following components:
>* Program counter which consist of the address of the next executable instruction
>* Stack
>* Set of registers
>* A unique id

__States of Thread__
To understand the functionality of threads in depth, we need to learn about the lifecycle of the threads or the different thread states. Typically, a thread can exist in five distinct states. The different states are:
* __New Thread__ - A new thread begins its life cycle in the new state. However, at this stage, it has not yet started and it has not been allocated any resources. We can say that it is just an instance of an object.
* __Runnable__ - As the newly born thread is started, the thread becomes runnable (i.e. waiting to run). In this state, it has all the resources but still task scheduler have not scheduled it to run.
* __Running__ - In this state, the thread makes progress and executes the task, which has been chosen by task scheduler to run. Now, the thread can go to either the dead state or the non-runnable/ waiting state.
* __Non-running/waiting__ - In this state, the thread is paused because it is either waiting for the response of some I/O request or waiting for the completion of the execution of other thread.
* __Dead__ - A runnable thread enters the terminated state when it completes its task or otherwise terminates.

Example of thread lifecycle
![img](/assets/img/thread.jpg)

By contrast, __Multithreading__ is the ability of a CPU to manage the use of operating system by executing multiple threads concurrently. The main idea of multithreading is to achieve parallelism by dividing a process into multiple threads. The concept of multithreading can be understood with the help of the following example.

![img](/assets/img/multithreading.jpg)
Advantages of Multithreading:
* __Speed of communication__ − Multithreading improves the speed of computation because each core or processor handles separate threads concurrently.
* __Program remains responsive__ − It allows a program to remain responsive because one thread waits for the input and another runs a GUI at the same time.
* __Access to global variables__ − In multithreading, all the threads of a particular process can access the global variables and if there is any change in global variable then it is visible to other threads too.
* __Utilization of resources__ − Running of several threads in each program makes better use of CPU and the idle time of CPU becomes less.
* __Sharing of data__ − There is no requirement of extra space for each thread because threads within a program can share same data.

Cons of Multithreading
* __Not suitable for single processor system__ − Multithreading finds it difficult to achieve performance in terms of speed of computation on single processor system as compared with the performance on multi-processor system.
* __Issue of security__ − As we know that all the threads within a program share same data, hence there is always an issue of security because any unknown thread can change the data.
* __Increase in complexity__ − Multithreading can increase the complexity of the program and debugging becomes difficult.
* __Lead to deadlock state__ − Multithreading can lead the program to potential risk of attaining the deadlock state.
* __Synchronization required__ − Synchronization is required to avoid mutual exclusion. This leads to more memory and CPU utilization.

### Working with Threads

__Create & Destory Threads__
Lets say You want to create and destroy threads for concurrent execution of code. The threading library can be used to execute any Python callable in its own thread. To
do this, you create a `Thread` instance and supply the callable that you wish to execute as a target.

```python
# Code to execute in an independent thread
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and launch a thread
t = Thread(target=countdown, args=(10,))
t.start()

```
When you create a thread instance, it doesn’t start executing until you invoke its `start()` method (which invokes the target function with the arguments you supplied). Threads are executed in their own system-level thread (e.g., a POSIX thread or Windows threads) that is fully managed by the host operating system. Once started, threads run independently until the target function  returns. You can query a thread instance to see if it’s still running:

```python
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create and launch a thread
t = Thread(target=countdown, args=(10,))
t.start()

# Query the thread to see if it is still running
if t.is_alive():
    print('Still running')
else:
    print('Completed')
```

You can also request to join with a thread, which waits for it to terminate:

```python
t.join()
```
The interpreter remains running until all threads terminate. For long-running threads or background tasks that run forever, you should consider making the thread daemonic. For example:

```python
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
```

Daemonic threads can’t be joined. However, they are destroyed automatically when the main thread terminates.

A __daemon__ is a background process that handles the requests for various services such as data sending, file transfers, etc. Another important point about daemon threads is that we can opt to use them only for non-essential tasks that would not affect us if it does not complete or gets killed in between.

Due to a global interpreter lock (GIL), Python threads are restricted to an execution model that only allows one thread to execute in the interpreter at any given time. For
this reason, Python threads should generally not be used for computationally intensive tasks where you are trying to achieve parallelism on multiple CPUs. 

They are much better suited for I/O handling and handling concurrent execution in code that performs blocking operations (e.g., waiting for I/O, waiting for results from a database, etc.). Sometimes you will see threads defined via inheritance from the Thread class. For
example:

```python
from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0
 
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()
```
Although this works, it introduces an extra dependency between the code and the threading library. That is, you can only use the resulting code in the context of threads,whereas the technique shown earlier involves writing code with no explicit dependency on threading. By freeing your code of such dependencies, it becomes usable in other contexts that may or may not involve threads. For instance, you might be able to execute your code in a separate process using the multiprocessing module using code like this:
```python
import multiprocessing
c = CountdownTask(5)
p = multiprocessing.Process(target=c.run)
p.start()
```
Again, this only works if the `CountdownTask` class has been written in a manner that is neutral to the actual means of concurrency (threads, processes, etc.).

### What is Multi-Processing?
__Multiprocessing__ is the use of two or more CPUs units within a single computer system. It is the best approach to get the full potential from our hardware by utilizing full number of CPU cores available in our computer system.

__Eliminating impact of global interpreter lock (GIL)__
While working with concurrent applications, there is a limitation present in Python called the __GIL (Global Interpreter Lock)__. GIL never allows us to utilize multiple cores of CPU and hence we can say that there are no true threads in Python. GIL is the mutex – mutual exclusion lock, which makes things thread safe. In other words, we can say that GIL prevents multiple threads from executing Python code in parallel. The lock can be held by only one thread at a time and if we want to execute a thread then it must acquire the lock first.

With the use of multiprocessing, we can effectively bypass the limitation caused by GIL.  By using multiprocessing, we are utilizing the capability of multiple processes and hence we are utilizing multiple instances of the GIL.

Due to this, there is no restriction of executing the bytecode of one thread within our programs at any one time.

__Relation between process & thread__
In multithreading, a process and thread are two very closely related terms having the same goal to make computer able to do more than one thing at a time. 

A __process__ can contain one or more threads but a tread cannot contain a process. Both however, remain the two basic units of execution for a program. A program, executing a series of instructions, initiates both processes and threads.

| Process                                                                                                             | Thread                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Process is heavy weight or resource intensive.                                                                      | Thread is lightweight which takes fewer resources than a process.                                                 |
| Process switching needs interaction with operating system.                                                          | Thread switching does not need to interact with operating system.                                                 |
| In multiple processing environments, each process executes the same code but has its own memory and file resources. | All threads can share same set of open files, child processes.                                                    |
| If one process is blocked, then no other process can execute until the first process is unblocked.                  | While one thread is blocked and waiting, a second thread in the same task can run.                                |
| Multiple processes without using threads use more resources.                                                        | Multiple threaded processes use fewer resources.                                                                  |
| In multiple processes, each process operates independently of the others.                                           | One thread can read, write or change another thread's data.                                                       |
| If there would be any change in the parent process then it does not affect the child processes.                     | If there would be any change in the main thread then it may affect the behavior of other threads of that process. |
| To communicate with sibling processes, processes must use inter-process communication.                              | Threads can directly communicate with other threads of that process.                                              |

### Working with Processes

The following three methods can be used to start a process in Python within the multiprocessing module
* Fork
* Spawn
* Forkserver

__Creating a process with Fork__
Fork command is a standard command found in UNIX. It is used to create new processes called child processes. This child process runs concurrently with the process called the parent process. These child processes are also identical to their parent processes and inherit all of the resources available to the parent. The following system calls are used while creating a process with Fork:
* `fork()` − It is a system call generally implemented in kernel. It is used to create a copy of the process.p>
* `getpid()` − This system call returns the process ID(PID) of the calling process.

Example
```python
import os

def child():
   n = os.fork()
   
   if n > 0:
      print("PID of Parent process is : ", os.getpid())

   else:
      print("PID of Child process is : ", os.getpid())
child()
```
__Creating a process with Spawn__
Spawn means to start something new. Hence, spawning a process means the creation of a new process by a parent process. The parent process continues its execution asynchronously or waits until the child process ends its execution. Follow these steps for spawning a process:
* Importing multiprocessing module.
* Creating the object process.
* Starting the process activity by calling start() method.
* Waiting until the process has finished its work and exit by calling join() method.

Example
```python
import multiprocessing

def spawn_process(i):
   print ('This is process: %s' %i)
   return

if __name__ == '__main__':
   Process_jobs = []
   for i in range(3):
   p = multiprocessing.Process(target = spawn_process, args = (i,))
      Process_jobs.append(p)
   p.start()
   p.join()
```

__Creating a process with Forkserver__
Forkserver mechanism is only available on those selected UNIX platforms that support passing the file descriptors over Unix Pipes. Consider the following points to understand the working of Forkserver mechanism:
* A server is instantiated on using Forkserver mechanism for starting new process.
* The server then receives the command and handles all the requests for creating new processes.
* For creating a new process, our python program will send a request to Forkserver and it will create a process for us.
* At last, we can use this new created process in our programs.


### Working with Pools

Suppose we had to create a large number of threads for our multithreaded tasks. A major issue could be in the throughput getting limited. To solve this We can create a pool of threads. 

__A thread pool__ may be defined as the group of pre-instantiated and idle threads, which stand ready to be given work. Creating thread pool is preferred over instantiating new threads for every task when we need to do large number of tasks. A thread pool can manage concurrent execution of large number of threads as follows:
* If a thread in a thread pool completes its execution then that thread can be reused.
* If a thread is terminated, another thread will be created to replace that thread.

Python standard library includes the `concurrent.futures` module. This module was added in Python 3.2 for providing the developers a high-level interface for launching asynchronous tasks. It is an abstraction layer on the top of Python’s threading and multiprocessing modules for providing the interface for running the tasks using pool of threads or processes.

__Executor Class__
Executors are an abstract class of the concurrent.futures Python module. It cannot be used directly and we need to use one of the following concrete subclasses:
* ThreadPoolExecutor
* ProcessPoolExecutor

__ThreadPoolExecutor__ – is one of the concrete subclasses of the Executor class. The subclass uses multi-threading and we get a pool of threads for submitting tasks. This pool assigns tasks to the available threads and schedules them to run.

Example:
```python
from concurrent.futures import ThreadPoolExecutor
from time import sleep

def task(message):
    sleep(2)
    return message

def main():
    # Initializes the ThreadPoolExecutor Subclass with 5 Threads
    executor = ThreadPoolExecutor(5)

    # Submits, schedules and executes tasks
    future = executor.submit(task, ("Completed"))
    
    # Polling to check the status of tasks
    print(future.done())
    sleep(2)
    print(future.done())
    print(future.result())

if __name__ == '__main__':
    main()
```

The following example is borrowed from the Python docs. In this example we do the following:
1. The `concurrent.futures` module has to be imported. 
2. Then a function named `load_url()` is created which will load the requested url. 
3. The function then creates `ThreadPoolExecutor` with 5 threads in the pool.
4. The ThreadPoolExecutor has been utilized as context manager (using the `with` statement). 
5. We can get the result of the future by calling the result() method on it.

```python
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
   'http://www.cnn.com/',
   'http://europe.wsj.com/',
   'http://www.bbc.co.uk/',
   'http://some-made-up-domain.com/'] # this one will produce an error

def load_url(url, timeout):
   with urllib.request.urlopen(url, timeout = timeout) as conn:
       return conn.read()

with concurrent.futures.ThreadPoolExecutor(max_workers = 5) as executor:
   future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
   for future in concurrent.futures.as_completed(future_to_url):
       url = future_to_url[future]
       try:
          data = future.result()
       except Exception as exc:
          print('%r generated an exception: %s' % (url, exc))
       else:
          print('%r page is %d bytes' % (url, len(data)))
```
Output
```
'http://some-made-up-domain.com/' generated an exception: <urlopen error [Errno 11004] getaddrinfo failed>
'http://www.foxnews.com/' page is 229313 bytes
'http://www.cnn.com/' page is 168933 bytes
'http://www.bbc.co.uk/' page is 283893 bytes
'http://europe.wsj.com/' page is 938109 bytes
```

The Python `map()` function is widely used in a number of tasks. One such task is to apply a certain function to every element within iterables. Similarly, we can map all the elements of an iterator to a function and submit these as independent jobs to out `ThreadPoolExecutor`. Consider the following example of Python script to understand how the function works.

```python
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

values = [2,3,4,5]

def square(n):
   return n * n

def main():
   with ThreadPoolExecutor(max_workers = 3) as executor:
        results = executor.map(square, values)

    for result in results:
        print(result)

if __name__ == '__main__':
   main()
```

__A Process Pool__ is defined as the group of pre-instantiated and idle processes, which stand ready to be given work. Creating process pool is preferred over instantiating new processes for every task when we need to do a large number of tasks.

__ProcessPoolExecutor__ – is one of the concrete subclasses of the Executor class. It uses multi-processing to provide a pool of processes for submitting tasks. This pool assigns tasks to the available processes and schedules them to run.

Basic example of multiprocessing using pools
```python
from concurrent.futures import ProcessPoolExecutor
from time import sleep

def task(message):
   sleep(2)
   return message

def main():
   executor = ProcessPoolExecutor(5)
   future = executor.submit(task, ("Completed"))
   print(future.done())
   sleep(2)
   print(future.done())
   print(future.result())

if __name__ == '__main__':
    main()
```

__When to use ProcessPoolExecutor and ThreadPoolExecutor?__
Now that we know how to use both Executor classes – `ThreadPoolExecutor` and `ProcessPoolExecutor`, we need to know when to use which executor. We need to choose:
* __ProcessPoolExecutor__ in cases of CPU-bound workloads
* __ThreadPoolExecutor__ in case of I/O-bound workloads.

If we use ProcessPoolExecutor, then we do not need to worry about GIL because it uses multiprocessing

### Not worrying about GIL
You’ve heard about the Global Interpreter Lock (GIL), and are worried that it might be affecting the performance of your multithreaded program. Although Python fully supports thread programming, parts of the C implementation of the interpreter are not entirely thread safe to a level of allowing fully concurrent execution. In fact, the interpreter is protected by a so-called Global Interpreter Lock (GIL) that only allows one Python thread to execute at any given time. The most noticeable effect of the GIL is that multithreaded Python programs are not able to fully take advantage of multiple CPU cores (e.g., a computationally intensive application using more than one thread only runs on a single CPU). 

Before building GIL workarounds, it is important to emphasize that the GIL tends to only affect programs that are heavily CPU bound (i.e., dominated by computation). If your program is mostly doing I/O, such as network communication, threads are often a sensible choice because they’re mostly going to spend their time sitting around waiting. In fact, you can create thousands of Python threads with barely a concern. Modern operating systems have no trouble running with that many threads, so it’s simply not something you should worry much about.

For CPU-bound programs, you really need to study the nature of the computation being performed. For instance, careful choice of the underlying algorithm may produce a far greater speedup than trying to parallelize an non-optimal algorithm with threads. Similarly, given that Python is interpreted, you might get a far greater speedup simply by moving performance-critical code into a C extension module. Extensions such as `NumPy` are also highly effective at speeding up certain kinds of calculations involving array data.

It’s also worth noting that threads are not necessarily used exclusively for performance. A CPU-bound program might be using threads to manage a graphical user interface, a network connection, or provide some other kind of service. In this case, the GIL can actually present more of a problem, since code that holds it for an excessively long period will cause annoying stalls in the non-CPU-bound threads. In fact, a poorly written C
extension can actually make this problem worse, even though the computation part of the code might run faster than before.

---

# Asyncio in Python

Event-driven programming focuses on events. Until now, we were dealing with either sequential or parallel execution model but the model having the concept of event-driven programming is called `asynchronous model`. 

__Event-driven programming__ depends upon an event loop that is always listening for the new incoming events. The working of event-driven programming is dependent upon events. Once an event loops, the event decide what to execute and in what order. 

![img](/assets/img/event.jpg)

### Using Asyncio

__Asyncio__ is a module that was added in Python 3.4 to provide infrastructure for writing single-threaded concurrent code using co-routines.

__Event-loop__ - is a functionality to handle all the events in a computational code. During execution of a whole program, the event loop keeps track of all the incoming and execution of events. The Asyncio module allows a single event loop per process. Followings are some methods provided by Asyncio module to manage an event loop:
    * `loop = get_event_loop()` - This method will provide the event loop for the current context.
    * `loop.call_later(time_delay,callback,argument)` − This method arranges for the callback that is to be called after the given time_delay seconds.
    * `loop.call_soon(callback,argument)` − This method arranges for a callback that is to be called as soon as possible. The callback is called after `call_soon()` returns and when the control returns to the event loop.
    * `loop.time()` − This method is used to return the current time according to the event loop’s internal clock.
    * `asyncio.set_event_loop()` − This method will set the event loop for the current context to the loop.
    * `asyncio.new_event_loop()` − This method will create and return a new event loop object.
    * `loop.run_forever()` − This method will run until stop() method is called.


Hello World Example with Asyncio
```python
import asyncio

def hello_world(loop):
   print('Hello World')
   loop.stop()

loop = asyncio.get_event_loop()

loop.call_soon(hello_world, loop)

loop.run_forever()
loop.close()
```
Asyncio is compatible with the `concurrent.futures.Future` class that represents a computation that has not been accomplished. There are following differences between asyncio.futures.Future and concurrent.futures.Future:
* `result()` and `exception()` methods do not take a timeout argument and raise an exception when the future isn’t done yet.
* Callbacks registered with `add_done_callback()` are always called via the event loop's `call_soon()`.
* `asyncio.futures.Future` class is not compatible with the `wait()` and `as_completed()` functions in the `concurrent.futures` package.

The following is an example that will help you understand how to use `asyncio.futures.future class`.
```python
import asyncio


async def Myoperation(future):
   await asyncio.sleep(2)
   future.set_result('Future Completed')

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(Myoperation(future))

try:
   loop.run_until_complete(future)
   print(future.result())
finally:
   loop.close()
```

__Coroutines__ in Asyncio is similar to the concept of standard Thread object under threading module. This is the generalization of the subroutine concept. A coroutine can be suspended during the execution so that it waits for the external processing and returns from the point at which it had stopped when the external processing was done. The following two ways help us in implementing coroutines:
* `async def function()` - This is a method for implementation of coroutines under Asyncio module.
* `@asyncio.coroutine` decorator - This is a method for implementation of coroutines to utilize generators with the `@asyncio.coroutine` decorator. 

Example of async def
```python
import asyncio

async def Myoperation():
   print("First Coroutine")

loop = asyncio.get_event_loop()
try:
   loop.run_until_complete(Myoperation())

finally:
   loop.close()
```

Example of `@async.coroutine`
```python
import asyncio

@asyncio.coroutine
def Myoperation():
   print("First Coroutine")

loop = asyncio.get_event_loop()
try:
   loop.run_until_complete(Myoperation())

finally:
   loop.close()
```
### Protocols
Asyncio module provides base classes that you can subclass to implement your network protocols. Those classes are used in conjunction with transports; the protocol parses incoming data and asks for the writing of outgoing data, while the transport is responsible for the actual I/O and buffering. Following are three classes of Protocol:

__Protocol__ − This is the base class for implementing streaming protocols for use with TCP and SSL transports.

__DatagramProtocol__ − This is the base class for implementing datagram protocols for use with UDP transports..

__SubprocessProtocol__ − This is the base class for implementing protocols communicating with child processes through a set of unidirectional pipes.