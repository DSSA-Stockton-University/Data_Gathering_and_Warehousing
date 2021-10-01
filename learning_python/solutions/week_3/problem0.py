# Problem 0 - Matching text at the start or end of a string
# ===== Instructions:
# Complete the functions below by filling in the missing code
# Then complete the missing code in the main() to traverse the list of
# filenames and match the strings using a tuple of multiple choices
# Explore methods likes startswith() and endswith() in your solution. 


import os

# Task 1 - Complete the function that returns a boolean when a matched is found at the start of the string
def getMatchingStart(x:str, s) -> bool:
    """
    Function that matches the begining characters in a string

    Args:
        x (str): A string of text
        s (str | tuple): String or multiple strings to search for a match

    Returns:
        bool: If match is found, result returns TRUE
    """
    result = x.startswith(s)
    return result

# Task 2 - Complete the function that returns a boolean when a matched is found at the end of the string
def getMatchingEnd(x:str, s) -> bool:
    """
    Function that matches the ending characters in a string

    Args:
        x (str): A string of text
        s (str | tuple): String or multiple strings to search for a match

    Returns:
        bool: If match is found, result returns TRUE
    """
    result = x.endswith(s)
    return result

def main():

    # list all files in the data folder
    fileNames = os.listdir('./data')
    print("Found Files:" , fileNames)
    
    # Task 3 - Use list comprehension to traverse the list of files and use getMatchingEnd to find files ending in ".txt" and ".json"
    ends = [name for name in fileNames if getMatchingEnd(x=name, s=('.txt', 'json'))]
    print(ends)

    # Task 4 - Use list comprehension to traverse the list of files and use getMatchingStart to find files starting with "St"
    starts = [name for name in fileNames if getMatchingStart(x=name, s=('St'))]
    print(starts)


if __name__ == '__main__':
    # execute main
    main()
    
 




