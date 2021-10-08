# Problem 0 - Iterating over merged sorted iterables
# ===== Instructions:
# Complete the functions below by filling in the missing code
# Refer to Lecture on Data Structures Part II for heaps
# You will need to implement a priority que to merge two python lists
# and iterate over the results using a for loop


import heapq
from typing import Iterable

# Task 1 - Create a priority Que
def priorityQueue(a:list, b:list) -> Iterable:
    """
    Function that implements a Priority Queue from merging two python lists

    Args:
        a (list): A valid python list
        b (list): A second valid python list

    Returns:
        queue (list): A sorted priority queue
    """

    """INSERT  YOUR CODDE HERE"""
    queue = heapq.merge(a,b)
    return queue

def main():

    # Initalize two python lists
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]

    # Create the priority Que
    q = priorityQueue(a,b)


    # Iterate over the queue using a for loop
    """INSERT YOUR CODE HERE"""
    for element in q:
        print(element)

        




if __name__ == '__main__':
    # execute main
    main()
    
 




