import random

choices = ["rock","paper","scissors","bag"]

computer = random.choice(choices)
player = input("rock,paper, or scissors?: ")

print(player)
print(computer)


