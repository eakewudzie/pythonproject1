#type casting in python----converting the data type of a value to another data type
x = 3 #int
y = 1.3 #float
z = "4" #sring

print(x)
print(y)
print(z)

#reasignment
x = str(x)
y = int(y)
z = float(z)

print(x*3) # displayed 3 times since it is a string
print(y)
print(z)

#printing a statement of string----type cast the other variable as string first to prevent error
print("x is : "+x)
print("y is : "+str(y))