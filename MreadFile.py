with open('file.txt') as file:
    print(file.read())

# print(file.closed) #to check the file if it has closed. Hence this code return true if closed and false if otherwise
#  the use of with --------It ensures the file is properly closed, even if
#  an exception occurs within the block.