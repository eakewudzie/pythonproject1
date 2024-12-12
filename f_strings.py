# F-strings help with automatic type conversion when embedding variables in strings, but they don’t eliminate the need for type casting in other parts of your code. They complement type casting rather than replace it.
# If you need to support versions of Python earlier than 3.6, f-strings won’t work because they’re not available in those versions. In that case, use .format() or % formatting.



age = 26
print(f"Your age is {age}")  # No need for str(age)
# Output: Your age is 26



x = 5
y = 10
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 5 and 10 is 15.




# NOTE
# Why use f-strings?
# Easy Variable Interpolation: You can insert variables or expressions directly into a string.
# Readable and Concise: F-strings are more concise and easier to read compared to older formatting methods like str.format() or %.

name = "Eunice"
age = 26

# Using an f-string
print(f"Hello {name}, you are {age} years old.")
# Output: Hello Eunice, you are 26 years old.

# Equivalent using .format()
print("Hello {}, you are {} years old.".format(name, age))

# Equivalent using % formatting
print("Hello %s, you are %d years old." % (name, age))
