# Instructions:
# Complete the exercises below, the first is done for you as an example. 
# You are not allowed to import libraries and must use python built-ins 
# Built-ins include, min(), max(), zip(), sorted()

def get_min_price(prices: dict) -> tuple:
       """
       A simple function that returns a tuple containing the stock ticker and price of
       the stock with the lowest price in a python dictionary. 
       

       Args:
           prices (dict): python dictionary of stock prices where
           the key is the ticker symbol and the value is the price

       Returns:
           tuple:
       """
       min_price = min(zip(prices.values(), prices.keys()))
       return min_price

# Task 1 - Create a function that returns the ticker with the highest stock price
def get_max_price(prices:dict)-> tuple:
       
    '''Insert Your Code Here'''
    max_price = max(zip(prices.values(), prices.keys()))
    return max_price


# Task 2 - Create a function that sorts all tickers from the dictionary in ascending order based on their stock price .
def sort_tickers_by_price(prices:dict) -> list:
       
       '''Insert Your Code Here'''

       prices_sorted = sorted(zip(prices.values(), prices.keys()))
       return prices_sorted

def main():
    # create python dict with key value pairs
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }  

    # Get the cheapest stock from the python dict
    min_price = get_min_price(prices=prices)
    print('min price:', min_price)

    # Get the most expensive stock from the python dict
    max_price = get_max_price(prices=prices)
    print('max price:', max_price)

    # Sort all stocks by price in ascending order
    sorted = sort_tickers_by_price(prices=prices)
    print('sorted prices:', sorted)


if __name__ == '__main__':
    # execute main
    main()
    
 




