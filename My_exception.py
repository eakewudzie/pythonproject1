# exception = events detected during execution that interrupt the flow of a program

# numerator = int(input("Enter a number to divide: "))
# denominator = int(input("Enter a number to divide by: "))

# result = numerator / denominator

# print(result)
# for instance , division by 0 would throw an error. To prevent this, we introduce try block
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result = numerator / denominator

    print(result)
except ZeroDivisionError:
    print("You cannot divide a number by Zero: You should know this")