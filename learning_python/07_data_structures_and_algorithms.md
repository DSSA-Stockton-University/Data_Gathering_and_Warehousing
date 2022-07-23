# DSSA Data Gathering & Warehousing
**Instructor**: Carl Chatterton
**Term**: Fall 2021
**Module**: 1
**Week**: 1

---
## Data Structures and Algorithms: Part 2

![img](/assets/img/ds_meme.jpg)
---

#### User Defined Data Structures in Python

__User-defined data structures__ are data structures that aren’t supported by python but can be programmed to reflect the same functionality using concepts supported by python.

---

##### Linked List, Queues (FIFO), Stacks (LIFO), & Graphs

A **Linked List**  is a sequence of data elements that are connected together using links. Each data element contains a connection to another data element in form of a pointer. Python does not have linked lists in its standard library.


>A _pointer_ is a variable whose value is the address of another variable, i.e., direct address of the something in memory

Each element of a linked list is called a **node**, and every node has two different fields:
1. `Data` contains the value to be stored in the node.
2. `Next` contains a reference to the next node on the list.

The first node is called the `head`, and it’s used as the starting point for any iteration through the list. The last node must have its `next` reference pointing to `None` to determine the end of the list. Here’s how it looks:

![img](/assets/img/Linkedlist.png)

__SPOILER ALERT__ - If you are are actively using blockchains then you are using linked list!

Basic Operations we can make with linked list:
> 1. **Traverse** − print all the elements of a linked list
> 2. **Insertion** − Adds an element at the beginning, end or between elements
> 3. **Removal** − Removes an existing element 
> 4. **Search** - Search for an element using its index

**Linked List Operations**
Below we implement a linked list from scratch and perform some basic operations
```python
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node
    
    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item not found")
        return False

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        # Deleting first node 
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

# Create an empty linked list
llist = LinkedList()

# Insert at the end of a linked list
llist.insert_at_end("Mon")
llist.insert_at_end("Tue")
llist.insert_at_end("Thu")
llist.insert_at_end("Sat")

# Insert at the end of a linked list
llist.insert_at_start("Sun")

# Insert after element 
llist.insert_after_item("Tue", 'Wed')
llist.insert_after_item("Thu", 'Fri')

# Traverse a linked list
llist.traverse_list()

# Search a linked list
llist.search_item("Tue")

# Remove an item from a linked list
llist.delete_element_by_value('Mon')

# Traverse a linked list
llist.traverse_list()
```
**Queues (FIFO) and Stacks (LIFO)**

In Python, there’s a specific object in the collections module that you can use for linked lists called `deque` (pronounced "deck"), which stands for double-ended queue.

`collections.deque()` uses an implementation of a linked list in which you can access, insert, or remove elements from the beginning or end of a list with constant O(1) performance.

A **Queue** is a linear structure that allows insertion of elements from one end and deletion from the other. Thus it follows, Fist In First Out(FIFO) methodology. The end which allows deletion is known as the front of the queue and the other end is known as the rear end of the queue. 
- For a queue, you use a First-In/First-Out (FIFO) approach. That means that the first element inserted in the list is the first one to be retrieved
> Example: Image you are driving through a car wash. The first car to enter the front of the cash wash is the first car to exit the car wash. 

![img](/assets/img/queue.jpg) ![img](/assets/img/carwash.jpg)

_Queues_ and _stacks_ differ only in the way elements are retrieved. 


A **Stack** is a linear structure that allows data to be inserted and removed from the same end thus follows a last in first out(LIFO) system. Insertion and deletion is known as push() and pop() respectively.

- For a stack, you use a Last-In/First-Out (LIFO) approach. That means that the last element inserted in the list is the first one to be retrieved
> Example: Image you are a dishwasher in a restaurant. Dirty dishes come in and are stacked on top of each other. When you wash a dish you cannot grab from the bottom or the stack will collapse, instead you start at the top and work your way down.  

![img](/assets/img/stack.jpg) ![img](/assets/img/dishes.jpg)

Basic Operations we can make with Queues and Stacks:
> 1. **Traverse** − print all the element
> 2. **Insertion** − add elements to a stack or queue 
> 3. **Removal** − remove elements from a stack or queue
> 4. **Search** - Search for an element in a linked list

**Operations using Queues**
```python
from collections import deque
# Create a queue 
queue = deque()

# add elements to a queue
queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue)

# remove elements from a queue
# Every time you use pop left you remove the head of the linked list
queue.popleft()
print(queue)

# Search elements in a queue using an index
print(queue[0])

```

**Operations using Stacks**
```python
from collections import deque
# Create a stack
stack = deque()

# add elements to a stack
stack.appendleft("Ford")
stack.appendleft("Tesla")
stack.appendleft("GMC")
print(stack)

# remove elements from a stack
stack.popleft()
print(stack)

# Search elements in a stack using an index
print(stack[0])

```
**Examples to try: Take 1 to 2 Minutes:**
Try to make a Queue and Stack using `collections.deque()`
Try to add elements and remove element

A **Graph** is a non-linear data structure consisting of `nodes` and `edges`. The nodes are sometimes also referred to as vertices and the edges are lines that connect any two nodes in the graph.  A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.

![img](/assets/img/graph.png)

We wont cover all the operations that can be done with graph data structures but lets look at a basic example:

Adding an edge to an existing graph involves treating the new vertex as a tuple and validating if the edge is already present. If not then the edge is added.
```python
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()

    # Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    # List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with graph elements
graph_elements = { 
   "Bob" : ["Jess","Ann"],
   "Ann" : ["Bob", "Tony"],
   "Jess" : ["Bob", "Tony"],
   "Wayne" : ["Sally"],
   "Sally" : ["Wayne"]
}

g = graph(graph_elements)
g.AddEdge({'Bob','Wayne'})
g.AddEdge({'Bob','Sally'})

print(g.edges())
```

---
##### Trees and Heaps

A **Binary Tree** is a non-linear data structure that is used for searching and data organization. A binary tree is comprised of nodes where each node has a data component, a left child pointer and a right child pointer. 

> Key terms for Trees:
> Node – The basic unit of a binary tree.
> Root – The root of a binary is the topmost element. There is only one root in a binary tree.
> Leaf – The leaves of a binary tree are the nodes which have no children.
> Level – The level is the generation of the respective node. The root has a level of 0, the children of the root node has a level of 1, the grandchildren of the root node has a level 2 and so on.
> Parent – The parent of a node is the node that is one level upward of the node.
> Child – The children of a node are the nodes that are one level downward of the node.

Example of a binary tree:
![img](/assets/img/tree.jfif)

A binary tree is a **hierarchical data structure**, that is organized in the form of a tree. Trees can be used for efficient searching, when the elements are organized with some order.

Basic example in python:
```python
# The Node Class defines the structure of a Node
class Node:
    # Initialize the attributes of Node
    def __init__(self, data):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data

root = Node(8) # Instantiating the Tree
# Tree Structure
#        8
#      /    \
#     None   None

root.left = Node(7) # Setting the left child of the root
root.right = Node(12) # Setting the right child of the root

# Tree Structure
#          8
#        /    \
#       7      12
#     /    \  /    \
#  None  None None None
```
Traversal of a Binary Tree:
1. inorder traversal - The left child is visited first, followed by the parent node, then followed by the right child.
2. preorder traversal - The root node is visited first, followed by the left child, then the right child.
3. postorder traversal - The left child is visited first, followed by the right child, then the root nod

**Pre-order traversal**
```python
# Class for binary tree node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert method for new Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data
    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal - Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal - Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    # Postorder traversal - Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("Preoder:", root.PreorderTraversal(root))
print("Postoder:",root.PostorderTraversal(root))
print("Inorder:", root.inorderTraversal(root))
```
**Heap** is a tree structure in which each parent node is less than or equal to its child node. Then it is called a Min Heap. If each parent node is greater than or equal to its child node then it is called a Max heap. It is very useful when implementing priority queues where the queue item with higher weighting is given more priority in processing.

A heap is created by using python’s standard library named `heapq`. This library has the relevant functions to carry out various operations on heap data structure. Below cover some common ones:
> __heapify__ − converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
> __heappush__ − adds an element to the heap without altering the current heap.
> __heappop__ − returns the smallest data element from the heap.
> __heapreplace__ − replaces the smallest data element with a new value supplied in the function.

**Basic Operations with Heaps**
> 1. **Traverse** − print all the elements from a heap
> 2. **Insertion** − add elements to a heap
> 3. **Removal** − remove elements from a heap
> 4. **Substitution** - remove elements in a heap
> 4. **Search** - Search for an element in a heap
```python
import heapq

# init a python list
H = [21,1,45,78,3,5]

# Use heapify to rearrange the elements
heapq.heapify(H)

# traverse all elements from the heap
print(H)

# Add element to the heap
heapq.heappush(H,8)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)
```


---
#### Algorithms in Python
An **algorithm** is a step-by-step procedure, which defines a set of instructions to be executed in a certain order to get the desired output. Algorithms are generally created independent of underlying languages, i.e. an algorithm can be implemented in more than one programming language.

From the data structure point of view we have covered many of the common categories of algorithms:
>Search − Algorithm to search an item in a data structure.
>Sort − Algorithm to sort items in a certain order.
>Insert − Algorithm to insert item in a data structure.
>Update − Algorithm to update an existing item in a data structure.
>Delete − Algorithm to delete an existing item from a data structure.


##### Characteristics of an algorithm
An algorithm should have the following characteristics:
> **Unambiguous** − Algorithm steps should be written clearly. Each steps and the inputs/outputs should be clearly written to have only one meaning.
> **Input** − An algorithm should have 0 or more well-defined inputs.
>**Output** − An algorithm should have 1 or more well-defined outputs, and should match the desired output.
>**Finiteness** − Algorithms should terminate after a completed some finite number of steps.
>**Feasibility** − Should be feasible with the available resources.
>**Independence** − An algorithm should have step-by-step directions, which should be independent of any programming code.

##### How to write an algorithm
There are no well-defined standards for writing algorithms. Rather, it is problem and resource dependent. Algorithms should never be written to support a particular programming code.

When we write algorithms, we write them in a step-by-step manner. First we must make sure we understand the domain and problem we are trying to solve for before designing the solution.
**Examples to try: Take 1 to 2 Minutes:**
Problem − Design an algorithm to add two numbers and display the result.

> Example to try:
> 1. − START
> 2. − declare three variables a, b & c
> 3. − define values of a & b
> 4. − add values of a & b
> 5. − store output of step 4 to c
> 6. − print c
> 7. − STOP
```python
# Example in python
a = 2
b = 3
c = a + b
print(c)
```

##### Sorting & Searching Algorithms
**Sorting** refers to arranging data in a particular format. Sorting algorithm specifies the way to arrange data in a particular order. Most common orders are in numerical or lexicographical order.

The importance of sorting lies in the fact that data searching can be optimized to a very high level, if data is stored in a sorted manner. Sorting is also used to represent data in more readable formats. Below are some common sorting algorithms we encounter in python:
>**Bubble Sort** - Algorithm where each pair of adjacent elements is compared and the elements are swapped if they are not in order
>
>**Merge Sort** - Divides the array into equal halves and then combines them in a sorted manner
>
>**Insertion Sort** - Involves finding the right place for a given element in a sorted list. It starts by comparing the first two elements. Then we pick the third element and find its proper position among the previous two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.
>
>**Shell Sort** - Involves sorting elements which are away from each other. We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted. The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it. Then we keep resetting the gap until the entire list is sorted.
>
>**Selection Sort** - Starts by finding the minimum value in a given list and moves it to a sorted list. Then the process repeats for each of the remaining elements in the unsorted list. The next element entering the sorted list is compared with the existing elements and placed at its correct position. At the end, all the elements from the unsorted list are sorted.

**Search** is a very basic necessity when you store data in different data structures. The simplest approach is traverse the data structure and match it with the value you are searching for. This is known as Linear search.

>**Linear search** is a sequential search made over all items one by one. 
    1. Every item is checked and if a match is found then that particular item is returned
    2. Otherwise, the search continues till the end of the data structure. 
>
>**Interpolation Search** algorithm works on the probing position of the required value. For this algorithm to work properly, the data collection should be in a sorted form and equally distributed. 
    1. Initially, the probe position is the position of the middle most item of the collection.
    2. If a match occurs, then the index of the item is returned.
    3. If the middle item is greater than the item, then the probe position is again calculated in the sub-array to the right of the middle item. 
    4. Otherwise, the item is searched in the subarray to the left of the middle item. 
    5. This process continues on the sub-array as well until the size of subarray reduces to zero.

##### Recursion, Divide & Conquer, and Backtracking

**Recursion** Recursion allows a function to call itself. We demonstrated an example of this using Binary Trees

**Backtracking** is a form of recursion. But it involves choosing only one option out of any possibilities. Begin by choosing an option and backtrack from it, if we reach a state where we conclude that this specific option does not give the required solution. We repeat these steps by going across each available option until we get the desired solution.

**Divide & Conquer** is where the problem is divided into smaller sub-problems and then each problem is solved independently. When we keep on dividing the subproblems into smaller sub-problems, we may eventually reach a stage where no more division is possible. 
