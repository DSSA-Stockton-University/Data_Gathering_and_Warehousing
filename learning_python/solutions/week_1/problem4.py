
# Problem 4 - Using different ways to filter data
# 
# ===== Description:
# There a many ways to filter data from an array. This exercise explores data filtering using list comprehension 
# 
# ===== Instructions:
# Complete the exercises below by completing the missing code for the python functions to accomplish the following:
# Find all positive values in a list where n > 0
# Find all negative values in a list where n < 0
# Substitute all negative values with 0 in the list
# Substitute all positive values with 0 in the list
#
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.
# Each answer requires using a for loop or/and if else statement
# Explore how to solve using list comprehension

from itertools import compress


def get_positive_values(data:list) -> list:
    positive = [n for n in data if n > 0]
    return positive

def get_negative_values(data:list) -> list:
    negative = [n for n in data if n < 0]
    return negative

def substitute_neg_values(data:list, threshold:int) -> list:
    neg_clip = [n if n > 0 else 0 for n in data]
    return neg_clip

def substitute_pos_values(data:list, threshold:int) -> list:
    pos_values = [n if n < 0 else 0 for n in data]
    return pos_values

def main():

    # Initializes a list of pos and neg values
    somelist = [1, 4, -5, 10, -7, 2, 3, -1]

    # All positive values
    pos = get_positive_values(somelist)
    print(pos)

    # All negative values
    neg = get_negative_values(somelist)
    print(neg)

    # Negative values clipped to 0
    neg_clip = substitute_neg_values(somelist, threshold=0)
    print(neg_clip)

    # Positive values clipped to 0
    pos_clip = substitute_pos_values(somelist, threshold=0)
    print(pos_clip)

if __name__ == '__main__':
    # main execution
    main()

