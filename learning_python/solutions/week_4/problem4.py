
# Problem 4 - Taking a Slice of an Iterator
# 
# ===== Description:
# You want to take a slice of data produced by an iterator, but the normal slicing operators wont work
# Iterators and generators can’t normally be sliced, because no information is known about
# their length (and they don’t implement indexing). Thankfully itertools provides a function
# called islice() that is an iterator that produces the desired slices by consuming and discarding
# all items up to the starting slice index and continue to the stopping slice index. 
# ===== Instructions:
# Complete the function below using islice() function from the itertools library


import itertools

def count(n):
    while True:
        yield n
        n += 1

# Task 1 - Extract all items generated from the python generator that are between the starting and ending indexes as a list
def getSlice(generator, start:int, end:int)-> list:
    """
    Function that takes slices from a generator
    Args:
        generator ([type]): A valid python generator
        start (int): starting value of the slice
        end (int): ending value of the slice

    Returns:
        list: list of all items of the slice
    """

    """INSERT YOUR CODE HERE"""
    slice = list(itertools.islice(generator, start, end))
    return slice

    

def main():
    # Initialize generator starting at a value of 0
    c = count(0)

    # Set the starting and ending values of the slice we want to take from the generator
    start = 10
    end = 20

    # Get the slice
    slice = getSlice(c, start, end)
    print(slice)


if __name__ == '__main__':
    # main execution
    main()

