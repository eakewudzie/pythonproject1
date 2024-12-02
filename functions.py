#function = block of code which is executed only when it is called
# functions only execute their block of code only when called

# Parameter: A variable in the function definition that acts as a placeholder for input values.
# Argument: The actual value passed to the function when it is called, assigned to the parameter.


def hello():
    print("Hello, it is nice to meet you!")


hello()


def greetings(name):
    print("Hello, " +name)


greetings("Eunice")


def mult(num1,num2):
    return num1 + num2

x = mult(5,3)


print(x)