#Roll Call Dice Game

import random

def call_dice():
    print("Rolling Dice...")

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"First Dice: {dice1}\nSecond Dice: {dice2} ")


while True:
    user_input = input("Do you want to roll the dice? (y/n): ")
    if user_input == 'y':
        call_dice()
    else:
        break