#Number Guessing Game for Refreshing my Python Practice

import random

while True:
    decision = input("Do you want to play? (y/n): ").strip().lower()

    if decision == 'y':
        random_number = random.randint(1, 100)
        tries = 10
        while tries > 0:
            print(f"You have live(s) {tries} left.")
            try:
                choice = int(input("Enter your guessed number (1-100): "))
            except ValueError:
                print("Invalid Input! Please enter a valid number.")
                tries -= 1
                continue

            if choice == random_number:
                print(f"Correct! You guessed the number: {random_number}!")
                break
            elif choice > random_number:
                print("Your guessed number is too high!")
                tries -= 1
            elif choice < random_number:
                print("Your guessed number is too low!")
                tries -= 1
            else:
                print(f"Invalid. Please try again. Number (1-100) only.")
                tries -= 1
                continue
        if tries == 0:
            print(f"You have lost! The number was {random_number}")
    elif decision == 'n':
        print("You have left.")
        break
    else:
        print("Invalid. Please try again.")
        continue


