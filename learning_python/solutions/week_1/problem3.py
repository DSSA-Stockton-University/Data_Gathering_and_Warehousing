# Problem 2 - Find out what two dictionaries have in common
# 
# ===== Description:
# Get used to using python dictionaries by using built-in dictionary functions keys() and items()
# 
# 
# ===== Instructions:
# Complete the exercises below by completing the missing code for the python functions to accomplish the following:
# Find what keys both dictionaries have in common
# Find keys that are in the first dictionary but not the second dictionary
# Find what key-value pairs both dictionaries have in common
#
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.
# Explore python what operators can be used to make dictionary comparisions 

def get_common_keys(a, b) -> set:
   result = a.keys() & b.keys()
   return result

def get_missing_keys(a, b) -> set:
   result = a.keys() - b.keys()
   return result

def get_common_pairs(a, b) -> set:
   result = a.items() & b.items()
   return result

def main():
   a = {
      'x' : 1,
      'y' : 2,
      'z' : 3
   }

   b = {
      'w' : 10,
      'x' : 11,
      'y' : 2
   }

   print('Common keys in both dict a and dict b:', get_common_keys(a,b))
   print('Keys in dict a but not in dict b:', get_missing_keys(a,b))
   print('Common (key,value) pairs in both dict a and dict b:', get_common_pairs(a,b))

if __name__ == '__main__':
   main()

