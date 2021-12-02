# Problem 1 - Sorting a python list of dictionaries on a common key
#
# Instructions:
# Complete the exercises below by completing the missing code.
# You are not allowed to import libraries and must use python built-ins 
# Any libraries you may need are imported for you.
# explore using the operator library, specifically the function itemgetter

from operator import itemgetter
from pprint import pprint


# Task 1 - Create a function that returns a sorted list of dictionaries using any number of dict keys
def sort_rows_by_key(rows:list, *key_names) -> list:
    """
    A function that sorts a list of dictionaries by any number of key.
    The Docstring has been provided to provide helpful hints. 

    Args:
        rows (list): Python list where each element contains a dictionary
        *key_names (*args): accepts any variable number of key names represented

    Returns:
        list: sorted list of dictionaries by key(s)
    """
    sorted_rows = sorted(rows, key=itemgetter(*key_names))
    return sorted_rows

def main():

    # Creates a python list where each element in the list is a dictionary
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    # calls the completed function and returns a sorted list of dictionaries using 1 key
    one_key = sort_rows_by_key(rows, 'uid')
    print("--------------------------")
    print("Sorted based on a single key:")
    print("--------------------------")
    pprint(one_key)

     # calls the completed function and returns a sorted list of dictionaries using 2 keys
    two_keys = sort_rows_by_key(rows, 'lname', 'fname')
    print("--------------------------")
    print("Sorted based on two keys:")
    print("--------------------------")
    pprint(two_keys)

     # calls the completed function and returns a sorted list of dictionaries using all keys
    all_keys = sort_rows_by_key(rows, 'uid', 'lname', 'fname')
    print("--------------------------")
    print("Sorted based on all keys:")
    print("--------------------------")
    pprint(all_keys)

if __name__ == '__main__':
    # executes main
    main()

