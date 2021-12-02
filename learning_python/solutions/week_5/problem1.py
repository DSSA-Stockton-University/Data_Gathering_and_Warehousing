# Problem 1 - Writing files only if they do not exist
# ===== Instructions:
# Write data to a new file (called script.txt) but only if 
# it does not already exist in the data folder

def writeDataToNewFile(filename, data):
    """
    A File writer that writes new files

    Args:
        filename (str): filename to be written to the data folder
        data (str): string of data to be written to the file contents
    """

    """INSERT YOUR CODE HERE"""
    with open(file=filename, mode='xt') as f:
        f.write(data)

def main():
    # Filename that will be used to create the file
    filename = "data/somefile.txt"

    # String of text to be written as the file contents
    data = "In a Galaxy Far Far Away..."

    # Calls the writeDatatoNewFile function 
    writeDataToNewFile(filename, data)

if __name__ == '__main__':
    # Main execution
    main()