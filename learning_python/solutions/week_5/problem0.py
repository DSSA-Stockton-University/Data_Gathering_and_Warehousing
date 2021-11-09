# Problem 0 - Read text files using a variety of options
# ===== Description:
# The file sample.txt is a UTF-8 encoded text file with Windows
# line-endings are (\r\n)
# ===== Instructions:
# Write a function that uses any arguments of open() to parse a text file
# Then print each line of the file using the python built-in repr()


def readAnyTextFile(filename, **kwargs):
    """
    A function that can read any text file!

    Args:
        filename (str): path and filename to the text file
        **kwargs (optional): unknown number of arbitrary keyword arguments to be used with open()
    """

    """INSERT YOUR CODE HERE"""
    with open(file=filename, **kwargs) as f:
        for line in f:
            print(repr(line))


def main():
    file = 'data/sample.txt'

    # Task 2 - Read text file using UTF-8 encoding
    print("Reading a Text File using UTF-8 encoding")
    """INSERT YOUR CODE HERE"""
    readAnyTextFile(file, mode='rt')

    # Task 3 - Read text file with universal newlines turned off
    print("Reading a Text File with universal newlines disabled")
    """INSERT YOUR CODE HERE"""
    readAnyTextFile(file, mode='rt', newline='')

    # Task 4 - Read text file using ASCII encoding with error handling
    print('Reading a Text file using ASCII ecoding with error handling')
    """INSERT YOUR CODE HERE"""
    readAnyTextFile(file, mode='rt', encoding='ascii', errors='replace')

    # Task 5 - Read text file using ASCII encoding with error handling
    print('Reading a Text file using ASCII ecoding with error handling')
    """INSERT YOUR CODE HERE"""
    readAnyTextFile(file, mode='rt', encoding='ascii', errors='ignore')
    

if __name__ == '__main__':
    # execute main
    main()
    
