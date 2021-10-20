# Problem 2 - Collect Meta Data from Files
# ===== Instructions:
# Complete the functions to get meta data from a file
# 
# Function 1
# Traverse a list of files and use the os library in python 
# to get the size and modified date of a single file. Then
# Create a hashmap (dictionary) as the output using the filename as the key
# and another dictionary containing the size and modified date as the values
# Make note of the Unix timestap that is produced when collecting file metadata
# You will need to convert to a normal date str (not datetime)

import os.path
import glob
from pprint import pprint
from datetime import datetime


def get_file_metadata(file_list:list) -> dict:
   """
   A function that gets the file size and the last modified date of a file

   Args:
       file_list (list): list of file names

   Returns:
       meta (dict): A dictionary of dictionaries where each key is the file name 
       and the value is a dictionary containing the size and modified date
       of the file

   Example Output: 
   {
      'file.json' : {'lastmodified': '2021-01-01', 'size': 1034}
   }
   
   """

   meta = {}
   for filename in file_list:
      size = os.path.getsize(filename)
      mod = os.path.getmtime(filename)
      meta[filename] = {
         'size': size,
         'lastmodified': datetime.fromtimestamp(mod).strftime('%Y-%m-%d')
         }

   return meta

def get_all_files(path_pattern):
   textfiles = glob.glob(path_pattern)
   return textfiles

def main():
   # Create a wild card pattern to grab all the txt files from the data folder
   pattern = '*/*.txt'

   # Gets all the filenames matching the wildcard pattern
   files = get_all_files(pattern)

   # Gets all the metadata 
   meta = get_file_metadata(files)
   pprint(meta)

if __name__ == '__main__':
   # Main execution
   main()