import random

userInput = input("Play again?: ")


while userInput == "yes":

    choices = ["Rock", "Paper", "Scissors"]

    for i in choices:
        compChoice = i

    userChoice = input("Rock! Paper! Scissors!: ")

    if compChoice == userChoice:
        print("It's a tie!")
    
    if compChoice == "Rock" and userChoice == "Scissors" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")

    if compChoice == "Paper" and userChoice == "Rock" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")

    if compChoice == "Scissors" and userChoice == "Paper" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
