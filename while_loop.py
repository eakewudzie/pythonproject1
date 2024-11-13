#execute code as long as the condition remains true
# below us an unending loop

# while 2==2:
#     print("you are going to be great")
#
#



name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " +name)




# this can alternatively be written as....below

# The line `while not name:` keeps
# looping until `name` has a value. Here, `not name` is **True** when `name` is empty
# (like `None` or an empty string), which are considered "falsy." So, this loop continues prompting
# the user for input until they provide a non-empty response, making `name` "truthy" and stopping the loop.




# name = None
# # None, a special value in Python that represents the absence of a value.
#
#
# while not name:
#     name = input("Enter a name: ")
#
# print("Hello "+name)

