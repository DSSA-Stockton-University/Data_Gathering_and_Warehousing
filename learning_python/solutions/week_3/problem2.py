# Problem 2 - Rounding floating point numbers to a fixed number of decimal places
# 
# ===== Instructions:
# Complete the function by writing an algorithm to do the following tasks:
# 1. declare a function to use two arguments: price, paid
# 2. declares a variable called roundedPrice that rounds the price to 2 decimal places
# 3. declares a variable called change that takes the difference in price & paid as an integer
# 4. declares a variable called binary that formats the variable change as a binary string
# 5. returns the variable binary
# You will need to explore how to use python built-ins format() and round() to create a successful algorithm 
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.
 
# Task - create an algorithm that calculates the exact change in dollars 
def calculateChange(price, paid):
    roundedPrice = round(price, 2)
    change = int(paid-roundedPrice)
    binary = format(change, 'b')
    return binary


def main():
    price = 213.5532454365
    paid = 250.00000000000000000001

    change = calculateChange(price, paid)
    print(change)


if __name__=='__main__':
   main()
