# DICE ROLLING GAME
import random


while True:
    choice = input("Roll the dice? (y/n): ").lower().strip()

    if choice == 'y':
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        print(f"You rolled {first_dice} and {second_dice}.")
    elif choice == 'n':
        print("You have left.")
        break
    else:
        print("Invalid choice. Please try again.")
