def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print("\n")
        print(key)
        for y in options[question_num-1]:
            print(y)
        guess = input("Enter either (A,B,C or D): as your answer: ")
        guess = guess.upper() # get the input of the guesses and then make it uppercase
        guesses.append(guess)

        correct_guesses +=check_answer(questions.get(key), guess)
                
        question_num += 1
    display_score(correct_guesses,guesses)

def check_answer(answer,guess):  
    if answer == guess:
        print("Correct answer")
        return 1
    else:
        print("wrong answer")
        return 0

# def check_answer():
#     pass

def display_score(correct_guesses,guesses):
    print("----------------")
    print("RESULTS") 
    print("----------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

def play_again():
    pass



questions ={
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: " :"C",
    "Is the Earth round?:  ": "D"

}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2010" ],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True", "B. False", "C. Maybe", "D. Don't know"]
    
]

new_game() 