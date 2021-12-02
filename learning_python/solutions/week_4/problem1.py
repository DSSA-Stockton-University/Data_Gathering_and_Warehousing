# Problem 1 - Using Forward and Backward Iterators
#
# ===== Instructions:
# Complete the exercises below by completing the missing code for the class object countdown
# there are two methods in the class which are generators. __iter__ is a forward generator
# while __reversed__ is a reversed generator that need code completed.
# You will need to use python operators to increase or decrease the value of n between iterations
# You will also need to use yield instead of return (because iterators do not destroy local variables)
# Remember Methods are just functions of an object
# Objects are represented as classes in python
# Refer to into to python lecture for an OOP refresher if needed. 

class Countdown:
    def __init__(self, start):
        self.start = start

    # Task 1 Forward iterator - using a while loop, if n > 0 yield n then reduce n by 1
    def __iter__(self):
        n = self.start
        """INSERT YOUR CODE HERE"""
        while n > 0:
            yield n
            n -= 1

    # Task 1 Reversed iterator - using a while loop, if n <= start yield n then increase n by 1
    def __reversed__(self):
        n = 1
        """INSERT YOUR CODE HERE"""
        while n <= self.start:
            yield n
            n += 1

def main():
    c = Countdown(10)
    print("Forward:")
    for x in c:
        print(x)

    print("Reverse:")
    for x in reversed(c):
        print(x)


if __name__ == '__main__':
    # executes main
    main()

