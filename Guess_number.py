import random

start_number = int(input("start number: "))
end_number = int(input("end number: "))

def guess(x, y):
    random_number = random.randint(x, y)   
    user_input = -2

    while user_input != random_number:
        user_input = int(input(f"Guess the number between {x} and {y}: "))
        if user_input < random_number:
            print(" Too low")
        elif user_input > random_number:
            print("Too high")
    print(f"Well done! The number {random_number} is correct.")

guess(start_number, end_number)