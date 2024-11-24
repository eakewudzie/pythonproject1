#set= colleection which is unordered , unindexed    and doesn't allow uplicates

# Unordered: Sets do not maintain the order of their elements. The items in a set may appear in a different order each time you access them.

# Unindexed: Sets do not support indexing or slicing because they are unordered.

# No Duplicates: Sets automatically remove duplicate values. If you add duplicates, they will be stored only once.

utensils = {"fork","spoon","knife","saucepan"}
dishes = {"bowl","plate","cup"}

for x in utensils:
    print(x)


utensils.add("cutting board")
# utensils.remove("knife")
# utensils.clear()
print(utensils)


# utensils can be updated with a different list

utensils.update(dishes)
print(utensils)