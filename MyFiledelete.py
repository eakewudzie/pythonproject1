# Removed the duplicate else block – The else should 
# only be used once after try-except.


# import os is a statement in Python that imports
#  the built-in os module, which provides functions for
#  interacting with the operating system.
import os
path = "text.txt"
pathDir = "MyFold"
nEmpty = "nemptyFolder"
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
except OSError:
    print("the directory is not empty and hence cannot be removed")
else:
    print(pathDir + " was deleted")


try:
    os.rmdir(nEmpty)
except OSError:
    print(nEmpty +" Folder is not empty")
else:
    print("Folder has been removed")
