# scope = the region that a variable is recognized. 
#          A variable is only available inside the region it is created.
#         A global and locally scoped versions of a variable can be created


name = "Eunice"


def display_name():
    name = "Ewudzie"
    print(name)

display_name() #gives the local variable name


# this is for the global variable
print(name)



 #-------------DECLARING AND USING A GLOBAL VARIABLE IN A  FUNC------------------
 #-----------to modify a global variable inside a function, you must explicitly declare it 
 # using the global keyword. Without global, Python will treat any assignment to the variable as 
 # creating a new local variable.-------

 
x = 10  # Global variable

def my_function():
    global x  # Declare x as global
    x = x + 5  # Modify global x
    print(x)

my_function()
# Output: 15

print(x)  # Global variable is now modified
# Output: 15
