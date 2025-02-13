
# rock ,paper , scissors game
# print("Enter one of the choices provided: ")
import random
choices = ["rock","scissors","paper"]

computer = random.choice(choices)
person1 = None

while person1 not in choices:
    person1 = input("Enter your choice: rock,paper or scissors: " )
    

if person1 == computer:
    print("computer: ", computer)
    print("person1: ", person1)
    print("Tie!")
elif person1 == "rock":
    if computer == "paper":
        print("computer: ", computer)
        print("person1: ", person1)
        print("You lose!")



# print("computer: ",  computer)
# print(person1)




