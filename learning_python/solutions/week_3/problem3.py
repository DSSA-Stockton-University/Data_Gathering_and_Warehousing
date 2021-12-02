# Problem 3 - Working with Time deltas
# 
# ===== Description:
# Get used to using python datetime objects by working with te datetime library 
# 
# ===== Instructions:
# complete the missing lines of code in the function below using the datetime library
# You will need to use several conditional expressions and serval datetime methods
# to code a working solution. Read each task carefully then explore what methods are available for datetime objects
# You are not allowed to import external libraries
# Any libraries you may need are imported for you already from the python standard library.

from datetime import datetime, timedelta


def getPreviousDayByName(dayname, start_date=None):

   # Initialize a list of days
   weekdays = [
      'Monday', 
      'Tuesday', 
      'Wednesday', 
      'Thursday', 
      'Friday', 
      'Saturday', 
      'Sunday'
      ]

   # Task 1 - implement code such that if no start date is given, start_date is set to today's date by default
   if start_date is None:
      start_date = datetime.today()

   # Task 2 - implement code to get the weekday number (1-7) from the start_date 
   day_num = start_date.weekday()

   # Task 3 - implement code to get the index of dayname from the weekdays list
   day_num_target = weekdays.index(dayname)
   days_ago = (7 + day_num - day_num_target) % 7 

   if days_ago == 0:
      days_ago = 7

   target_date = start_date - timedelta(days=days_ago)
   return target_date

def main():

   # Gets the datetime of last friday
   previousFriday = getPreviousDayByName(dayname='Friday')
   print(previousFriday)
   
if __name__ == '__main__':
   # main execution
   main()

