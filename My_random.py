#random module ....[useful methods of the random variable]


import random

y = random.randint(1,10)
z = random.random() #generates a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive)
newList = ['apple','paper']
m = random.choice(newList)

print(y)
print(z)
# print(random.choice(newList))
print(m)


my_cards = [1,2,3,4,5,6,"M","N","O"]
random.shuffle(my_cards)
print(my_cards)


# random.shuffle() directly modifies the original list by rearranging its elements in a random order.
# The function does not create or return a new shuffled list—it only affects the list passed to it.
#  to see the shuffled list, you should directly print the original list after calling shuffle():