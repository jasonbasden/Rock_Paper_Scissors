import random

userInput = input("Do you want to play Rock, Paper, Scissors?: ").lower()


while userInput == "yes":

    compChoice = random.choice = ["Rock", "Paper", "Scissors"]

    userChoice = input("Rock! Paper! Scissors!: ")

    
    def play_again():

        userInput == input("Do you want to play again?: ").lower()
        if userInput != "yes":
            print("Thanks for playing!")
            userInput != "yes"
            return userInput 

    if compChoice == userChoice:
        print("It's a tie!")
        play_again()
        
    
    if compChoice == "Rock" and userChoice == "Scissors" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        play_again()

    if compChoice == "Paper" and userChoice == "Rock" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        play_again()
        

    if compChoice == "Scissors" and userChoice == "Paper" and compChoice != userChoice:
        print("The computer wins!")
    else:
        print("You win!")
        play_again()
        


 