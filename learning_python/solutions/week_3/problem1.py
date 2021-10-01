# Problem 1 - Using Regular Expressions for simple matching
#
# ===== Instructions:
# Complete the exercises below by completing the missing code and by building your own regular expressions
# The explore the re library to find the method for complining a regex and to find all matches from text
# Then write a working regex in the main(). You can practice building regex by going to https://regexr.com/

import re

# Task 1 - Use the re library to compile and find all text matches based on a regular expression
def findMatchingDates(text:str, regex) :
    """
    Function that finds all text matching a regular expression

    Args:
        text (str): text to be evaluated
        regex (str): a valid regular expression

    Returns:
        [type]: Returns all texted matched by the regex
    """
    datePattern = re.compile(regex)
    found = datePattern.findall(text)
    return found

def main():
    # Some sample text
    textSample = 'Today is 09/20/2021. Class is on 09/23/2021.'

    # Task 2 - Write a Regex to Find all matching dates
    pattern = r'\d+/\d+/\d+'   
    matches = findMatchingDates(text=textSample, regex=pattern)
    print(matches)

    # Task 3 - Write a Regex to find all matching dates with capture groups
    pattern1 = r'(\d+)/(\d+)/(\d+)'
    for day, month, year in findMatchingDates(text=textSample, regex=pattern1):
        print(f"{day}-{month}-{year}")


if __name__ == '__main__':
    # executes main
    main()

