# index operator[] = gives access to a sequence's eleent(str,list,tuples)

name = "eunice Kakra"

if (name[0].islower()):
    name = name.capitalize()

print(name)


name1 = "Eunice Panyin!"

first_name =name1[:6].lower() #string slicing ...excludes last index of sring
last_name = name1[7:].upper()
last_charact = name1[-1] # last item referenced this way

print(first_name)
print(last_name)
print(last_charact)