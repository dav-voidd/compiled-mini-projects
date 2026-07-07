#Number Guessing Game
import random



wins = 0
loses = 0

def play():
    global wins, loses
    print("=== RANDOM NUMBER GUESSING GAME ===")
    print("Guess the number from 1-100!")


    tries = 10
    random_number = random.randint(1, 100)

    for i in range(tries):
        print(f"You have {tries} tries")
        user_number = int(input("Guess the number: "))
        if user_number > 100:
            print("Invalid, your guess must be 1-100 only.")
            if tries == 0:
                print("You lost!")
        elif user_number == random_number:
            print("You have guessed the number!")
            wins += 1
            break
        elif user_number > random_number:
            tries -= 1
            print("Your guess is too high!")
            if tries == 0:
                print("You lost!")
        elif user_number < random_number:
            tries -= 1
            print("Your guess is too low!")
            if tries == 0:
                print("You lost!")




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
