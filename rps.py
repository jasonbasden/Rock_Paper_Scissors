import random

userInput = input("Do you want to play Rock, Paper, Scissors?: ").lower()


while userInput == "yes":

    compChoice = random.choice = ["Rock", "Paper", "Scissors"]

    userChoice = input("Rock! Paper! Scissors!: ")

    if compChoice == userChoice:
        print("It's a tie!")
        break
    
    if compChoice == "Rock" and userChoice == "Scissors" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        break

    if compChoice == "Paper" and userChoice == "Rock" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        break

    if compChoice == "Scissors" and userChoice == "Paper" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        break



    userInput2 = input("Play again? ").lower()
    
    if userInput2 == "yes":
        userInput = "yes"
    else:
        userInput = "no"
