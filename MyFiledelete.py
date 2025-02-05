# Removed the duplicate else block – The else should 
# only be used once after try-except.

import os
path = "text.txt"
pathDir = "AnemptyFolder"
# os.remove('path')

try:
    os.remove('path')
except FileNotFoundError:
    print("The File not found")


try:
    os.rmdir(pathDir) # this only allows folders which are empty to be moved
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have he persmission to delete this")
except:
    print("the directory is not empty and hence cannot be removed")
else:
    print(pathDir + " was deleted")
