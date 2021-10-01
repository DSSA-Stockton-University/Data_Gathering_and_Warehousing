
# Problem 4 - Getting Date Ranges from Dates stored as strings
# 
# ===== Description:
# Working with date times in various formats and building date ranges
# 
# ===== Instructions:
# Complete the exercise below by completing the missing code for the python functions to accomplish the following:
# Covert a date that is represented as a string into a datetime object. You will need to explore what methods datetime has
# that can be used for converting strings to datetime objects


from datetime import datetime, timedelta
from pprint import pprint


def convertStringToDateTime(x):
    date = datetime.strptime(x, '%Y-%m-%d')
    return date

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

def generateDateRange(begins, ends, interval):

    dateList = []
    for d in date_range(start=begins, stop=ends, step=timedelta(hours=interval)):
        dateList.append(d)
    return dateList


def main():
    # Create some strings that contain dates
    startDate = '2021-09-01'
    endDate = '2021-09-20'

    # number of hours between datetime intervals
    step = 6

    # Converts to datetime obj
    start = convertStringToDateTime(startDate)
    print("Start Date:", start)

    # Converts to datetime obj
    end = convertStringToDateTime(endDate)
    print("End Date:", end)

    # Creates a interval range of dates
    dateRange = generateDateRange(start, end, 6)
    pprint(dateRange)



if __name__ == '__main__':
    # main execution
    main()

