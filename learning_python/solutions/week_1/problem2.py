# Problem 2 - Finding the largest or smallest n items in a python dictionary 
# 
# ===== Description:
# Example of using heapq to find the N smallest or largest items
# Similarly N smallest or largest items can be found using sorted(iterable, key=key)[:n] or sorted(iterable, key=key, reverse=True)[:n] respectively
# ===== Instructions:
# Complete the exercises below by completing the missing code for the python functions get_largest_n_items and get_smallest_n_items.
# Find the the n smallest and largest items by stock price (already provided for you in the main)
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.
# explore using the heapq library for working with heaps. Are there any methods in heapq to accomplish this task?
# You may need to use lambda in your solution, lambda is the equivalent of an unnamed python function to takes an expression ex. lambda s: s['price']

import heapq
from pprint import pprint


def get_largest_n_items(n:int, x:list, key) -> list:
   """
   Function that returns n largest items from a python list of dictionaries using heaps

   Args:
       n (int): number of items to return
       x (list): a list of python dictionaries
       key ([type]): dictionary key name containing  sortable values

   Returns:
       list: sorted list containing n number of python dictionaries
   """

   largest = heapq.nlargest(n,x, lambda s: s[key])
   return largest

def get_smallest_n_items(n:int, x:list, key) -> list:
   """
   Function that returns n smallest items from a python list of dictionaries using heaps

   Args:
       n (int): number of items to return
       x (list): a list of python dictionaries
       key ([type]): dictionary key name containing  sortable values

   Returns:
       list: sorted list containing n number of python dictionaries
   """

   smallest = heapq.nsmallest(n,x, lambda s: s[key])
   return smallest

def main():

   portfolio = [
      {'name': 'IBM', 'shares': 100, 'price': 91.1},
      {'name': 'AAPL', 'shares': 50, 'price': 543.22},
      {'name': 'FB', 'shares': 200, 'price': 21.09},
      {'name': 'HPQ', 'shares': 35, 'price': 31.75},
      {'name': 'YHOO', 'shares': 45, 'price': 16.35},
      {'name': 'ACME', 'shares': 75, 'price': 115.65}
   ]

   cheap = get_smallest_n_items(4, portfolio, key='price')
   expensive = get_largest_n_items(2, portfolio, key='price')

   pprint(cheap)
   pprint(expensive)

if __name__=='__main__':
   main()
