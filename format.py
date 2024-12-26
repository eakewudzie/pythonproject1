# this is a method available to strings
# str.format() = opional method that gives users
#               more control when displying output

# animal = "cat"
# item = "moon"

# print("the " +animal+" jumped over the " +item)
# writing the above code using the format method

print("the {} jumped over the {}".format("cat","moon"))


# ------NB----------format method is always called on a string, so it must come after the closing quotation mark of the string it is formatting. This is because format is a method of the str class in Python,