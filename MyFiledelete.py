import os
path = "text.txt"
pathDir = "AnemptyFolder"
# os.remove('path')

# try:
#     os.remove('path')
# except FileNotFoundError:
#     print("The File not found")


try:
    os.rmdir(pathDir)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have he persmission to delete this")
else:
    print("we canno find the file")