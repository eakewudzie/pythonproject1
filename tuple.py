# tuple = collection which is ordered and unchangeable(used to group together related data)

student =("Eunice",26,"female")

print(student.count("Eunice"))
print(student.index("Eunice"))


print(student)

for x in student:
    print(x)


if "Eunice" in student:
    print("I am here") 