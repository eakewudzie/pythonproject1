# let us include an exception

try:
    with open('file.txt') as file:
         print(file.read())
except FileNotFoundError:
      print("This file cannot be found or wrong name for file")
         


# with open('file.tx') as file:
#          print(file.read())



# print(file.closed) #to check the file if it has closed. Hence this code return true if closed and false if otherwise
#  the use of with open --------It ensures the file is properly closed, even if
#  an exception occurs within the block.