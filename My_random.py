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


cards = [1,2,3,4,5,6,"M","N","O"]
random.shuffle(cards)
print(cards)