# this is a method available to strings
# str.format() = opional method that gives users
#               more control when displying output

animal = "cat"
item = "moon"

# print("the " +animal+" jumped over the " +item)
# writing the above code using the format method

print("the {} jumped over the {}".format("cat","moon"))



# ------NB----------format method is always called on a string, so it must come after the closing quotation mark of the string it is formatting. This is because format is a method of the str class in Python,


# {} these are the format fields...

print("the {} jumped over the {}".format(animal,item)) # the values of the variables can be replaced by the name of he variables themselves and still work
# in this case.. it is positional argument
print("the {1} jumped over the {1}".format(animal,item))#positional argument


print("The {animal} jumped over the {item}".format(animal="elephant", item="star")) #keyword argument

# we can also have it as this
text = "the {} jumped over the {}"
print(text.format(animal,item))



# adding a padding to a text
surname ="Ewudzie"


print("Hello, my name is {}".format(surname))
print("Hello, my name is {:30}. it is nice to finally meet you".format(surname)) #padding
print("Hello, my name is {:<20}. Great to know you".format(surname))  #left align...bu by default already left aligned
print("Hello, my name is {:>20}. Great to know you".format(surname)) #right aligned
print("Hello, my name is {:^20}. Great to know you".format(surname)) # center use caret to cener align within the padding you have alloted


myNum = 5.987

#to format to display only first two decimal placesd...we can have this...
print("The number is {:.2f}".format(myNum))