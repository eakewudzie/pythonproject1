#logical operators(and,or,not)......to check for one or more conditional statements
temp = int(input("What is the temperature outside in degree celsius?: "))
if temp>=5 and temp <= 30:
    print("you can go outside")
elif temp <= 4:
    print("you cannot go outside")