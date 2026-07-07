#Number Guessing Game
import random



wins = 0
loses = 0

def play():
    global wins, loses
    print("=== RANDOM NUMBER GUESSING GAME ===")
    print("Guess the number from 1-100!")


    tries = 11
    random_number = random.randint(1, 100)
    for i in range(tries):
        if tries == 0:
            print("You have lost the game")
            loses += 1
            break
        tries -= 1
        print(f"You have {tries} tries")
        user_number = int(input("Guess the number: "))
        if user_number > 100:
            print("Invalid, your guess must be 1-100 only.")
        elif user_number == random_number:
            print("You have guessed the number!")
            wins += 1
            break
        elif user_number > random_number:
            print("Your guess is too high!")
        elif user_number < random_number:
            print("Your guess is too low!")


while True:
    print("Welcome to Infinite Random Guessing Game")
    user_choice = input("Do you want to play? (y/n): ").strip().lower()

    if user_choice == 'y':
        play()
    elif user_choice == 'n':
        print("You have exited the game.")
        print(f"You have {wins} win(s) and {loses} loses.")
        break
    else:
        print("Invalid.")
