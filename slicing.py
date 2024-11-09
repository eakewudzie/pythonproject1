#slicing creates a substring by extracting elements from another string
# indexing[start:end:step]


#first index is inclusive while last index is exclusive

name = "Eunice Kakra"
first_name = name[0:6] #or just[:6] python assumes first is 0
#last letter for Eunice is e with index 5 but in order to get that...we have to end on 6

last_name = name[7:] #or name[7:12]
print(first_name)
print(last_name)

stepped_name = name[0:12:1]
#stepped_name = name[0:12:1] displays full name
print(stepped_name)

chg_stepped_name = name[::] #this gives the same output as the first
print(chg_stepped_name)

skip_of_second = name[::2]#displays second letter of each name
print(skip_of_second)

reversed_name = name[::-1]#this is one way to reverse name in python
print(reversed_name)


#slicing
website1= "http://Eunice.com"
website2= "http://wikipedia.com"

#define our slice method
slice = slice(7,-4)#start,end
print(website1[slice])
print(website2[slice])

