# # rock ,paper , scissors game
# # print("Enter one of the choices provided: ")
# import random
# while True:
#     choices = ["rock","scissors","paper"]

#     computer = random.choice(choices)
#     person1 = None

#     while person1 not in choices:
#         person1 = input("Enter your choice: rock,paper or scissors: " )
    

#     if person1 == computer:
#         print("computer: ", computer)
#         print("person1: ", person1)
#         print("Tie!")
#     elif person1 == "rock":
#         if computer == "paper":
#           print("computer: ", computer)
#           print("person1: ", person1)
#           print("You lose!")
#         if computer == "scissors":
#           print("computer: ", computer)
#           print("person1: ", person1)
#           print("You win")
#         elif computer == "paper":
#             print("computer:", computer)
#             print("person1:", person1)
#             print("You win!")

#     play_again = input("Would you like to play again? Yes or No: ").lower()
#     if play_again != "yes":
#         break

# print("Bye then")



# #     play_again = input("Would you like to play again? Yes or No: ").lower()

# #     if play_again!= "yes":
# #         break


# # print("Bye then")





# # print("computer: ",  computer)
# # print(person1)





import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    person1 = None

    while person1 not in choices:
        person1 = input("Enter your choice: rock, paper, or scissors: ").lower()

    if person1 == computer:
        print("computer:", computer)
        print("person1:", person1)
        print("Tie!")
    elif person1 == "rock":
        if computer == "paper":
            print("computer:", computer)
            print("person1:", person1)
            print("You lose!")
        elif computer == "scissors":
            print("computer:", computer)
            print("person1:", person1)
            print("You win!")
    elif person1 == "paper":
        if computer == "scissors":
            print("computer:", computer)
            print("person1:", person1)
            print("You lose!")
        elif computer == "rock":
            print("computer:", computer)
            print("person1:", person1)
            print("You win!")
    elif person1 == "scissors":
        if computer == "rock":
            print("computer:", computer)
            print("person1:", person1)
            print("You lose!")
        elif computer == "paper":
            print("computer:", computer)
            print("person1:", person1)
            print("You win!")
# check this section again
    play_again = input("Would you like to play again? Yes or No: ").lower()
    if play_again != "yes":
        break

print("Bye then. later")

