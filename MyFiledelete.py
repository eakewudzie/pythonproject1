import os
path = "text.txt"
# os.remove('path')

try:
    os.remove('path')
except FileNotFoundError:
    print("File not found here")