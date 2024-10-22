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
name = "Eunice Kakraa"
first_a_index = name.find("a")
second_a_index = name.find("a", first_a_index + 1)
print(second_a_index)

third_a_index = name.find("a", second_a_index + 1)
print(third_a_index)
