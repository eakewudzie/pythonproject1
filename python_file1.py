name_1,location,street_num = "Panyin","Bremen",5
print(name_1)
print(location)
print(street_num)

#22--------10------24
name = "Eunice Kakra"
print(len(name))
print(name.find("a"))
print(name.find("a"))


#this is to check the next occurrence of a in a text with multiple aas
name = "Eunice Kakraa "
first_a_index = name.find("a")
second_a_index = name.find("a", first_a_index + 1)
print(second_a_index)
#useful methods in python
third_a_index = name.find("a", second_a_index + 1)
print(third_a_index)
print(name.capitalize())  # if there is an additional space or string...only capitalizes the first word
print(name.upper())
print(name.lower())
print(name.isdigit())  #if value we have is a digit or not , return false if it isn't
print(name.isalpha())  #check to see if strings contains only alphabetical letters. it returns false if it has as a space
print(name.count("a"))
print(name.replace("a","i")) #replace an alphabet with a different one
print(name*3)
