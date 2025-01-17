import os
path = "C:\\Users\\EUNICE\\Desktop\\giteunice.png"


# The extra backslash (\) in Python file paths is due to how
#  the backslash (\) is interpreted in Python strings. In Python,
# the backslash is used as an escape
# character for special sequences, such as \n for a newline or \t for a tab.

if os.path.exists(path):
    print("This location exists")
else:
    print("this doesn't exist")







# An escape sequence is a combination
#  of characters in a string that starts with a
#  backslash (\) and has a special meaning. Escape sequences 
# are used to represent characters that cannot be directly included in
#  a string, such as a newline, tab, or certain special characters.

