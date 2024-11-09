#if statement: check if condition is true then execute

name = str(input("Enter your Name: "))
age =int(input("Enter your age: "))


if age >= 27:
    print("Great, You are a grown up " + name)
elif age == 26:
    print("you are the exact age we need. Continue with your application")
else:
    print("You are below our expected age and hence not eligible")