
# rock ,paper , scissors game

import random
choices = ["rock","scissors","paper"]

computer = random.choice(choices)

person1 = input("Enter your choice: rock,paper or scissors: " )
if person1 not in choices:
    print("select from the choices here")
else:
    print(person1)

print(computer)
# print(person1)




