# list = used to store multiple items in a single variable

food =["pizza", "chicken", "fries"]

# print(food)
# print(food[0])

food[0]="jollof"


# print(food)
food.append("ice cream")
food.append("grilled chicken")

# food.remove("jollof")
food.pop()
food.insert(0,"cake")
food.sort()
# food.clear() # this clears all enries in the list

# for loop to print each item in the list
for y in food:
    print(y)


