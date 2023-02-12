import random

while True:
    #set computer choices
    choices = ["rock", "paper", "scissors"]
    #set computer choices to random
    computer = random.choice(choices)
    
    #player vs computer
    player = input("Rock, Paper, Scissors??")
    if player == computer:
        print("Tied!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Lose!")
        else:
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Win!")
    elif player == "Paper":
        if computer == "Scissors":
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Lose!")
        else:
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Win!")
    elif player == "Scissors": 
        if computer == "Rock":
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Lose!")
        else: 
            print("You chose: ", player, ", Computer chose: ", computer, " -- You Win!")
    else:
        print("That's not a valid play!")

# loop gameplay
    retry = input("Play again? y/n: ")
    if retry.lower() != 'y':
        break
