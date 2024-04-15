import os
import random

def clear_console():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

#guess function
def guess(x, y):
    random_number = random.randint(x, y)   
    user_input = random_number-1
    clear_console()

    trying = 0
    while user_input != random_number:
        user_input = int(input(f"\nGuess the number between {x} and {y}: "))
        if user_input < random_number:
            print("\n   Too low\n")
        elif user_input > random_number:
            print("\n   Too high")
        trying += 1
    else:
        clear_console()
        print(f"\n  Well done! The number {random_number} is correct.")
        print(f"    You did it in {trying} tryings.")
        trying += 1

#welcome massage
clear_console()
print("#"*30)
print("WELCOME TO GUESS-NUMBER-GAME")
print("#"*30)
print("\n")

#Call the function to guess the number
while True:
    #Starting the game?
    start_game = input("Do you wanna play? (S/N) : ")
    if start_game.upper() != "S":
        clear_console()
        print("\n    Good bye, maybe another time...\n")
        quit()
    print("\nGreat decision, let´s getting start.")
    start_number = int(input("start number: "))
    end_number = int(input("end number: "))
    guess(start_number, end_number)
    