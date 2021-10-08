# Problem 2 - Creating new iteration patterns with Generators
# 
# ===== Instructions:
# Complete the function by filling in the missing code
# There are no python libraries that need to be included for this problem
# Use a while loop to implement a python generator that starts at a given value x 
# and increments by some amount to the stopping value. 


# Task 1 - Implement a while loop to yield the value of x then use a python operator to increment its value to the stopping point
def zRange(start, stop, increment):
    x = start
    """INSERT YOUR CODE HERE"""
    while x < stop:
        yield x
        x += increment


def main():
    start = 0
    stop = 10
    increment = 0.5
    for n in zRange(0, 4, 0.5):
        print(n)


if __name__=='__main__':
   main()
