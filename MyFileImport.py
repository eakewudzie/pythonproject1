import os

source = "test.txt"
destination = "C:\\Users\\EUNICE\\Desktop\\TextFolder\\test.txt"


try:
    if os.path.exists(destination):
        print("There is already a file as this")
    else:
        os.replace(source,destination)
        print(source+" has been moved")
except FileNotFoundError:
    print(source+" was not found")