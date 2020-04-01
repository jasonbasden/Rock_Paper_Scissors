import random

def play_again():

    userInput = input("Do you want to play again?: ").lower()
    if userInput != "yes":
        print("Thanks for playing!")
        return "no" # to cancel the while loop
    else:
        return "yes"

userInput = input("Do you want to play Rock, Paper, Scissors?: ").lower()

while userInput == "yes":

    weapons = ["Rock", "Paper", "Scissors"]
    compChoice = weapons[random.randint(0,2)].lower() # Grabs random weapon 

    userChoice = input("Rock! Paper! Scissors!: ")

    if compChoice == userChoice:
        print("It's a tie!")
        userInput = play_again()
    
    # These have to be lower case to be able to check it more accurately
    elif (compChoice == "rock" and userChoice == "scissors") or (compChoice == "paper" and userChoice == "rock") or (compChoice == "scissors" and userChoice == "paper"):
        print("The computer wins!")
        userInput = play_again()
    else:
        print("You win!")
        userInput = play_again()
