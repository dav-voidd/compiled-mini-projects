#Number Guessing Game
import random

from final_random_number_guessing_game import fake_tries

wins = 0
loses = 0




class Play:

    @staticmethod
    def decision():
        Play.check_score()
        new_content = int(Play.check_score())
        if fake_tries == new_content:
            pass
        elif fake_tries == 10:
            Play.add_score()
            print(f"You have a new high score with only {Play.check_score()} tries!")
        elif fake_tries > new_content:
            Play.add_score()
            print(f"You have a new high score with only {Play.check_score()} tries!")
        else:
            pass

    @staticmethod
    def add_score():
        with open("high_score.txt", "w") as file:
            file.write(f"{fake_tries}")


    @staticmethod
    def check_score():
        try:
            with open("high_score.txt", "r") as file:
                content = file.read().strip()
                if content == "":
                    return "10"
                return content
        except FileNotFoundError:
            return "10"




    @staticmethod
    def play():


        global wins, loses, fake_tries

        print("=== RANDOM NUMBER GUESSING GAME ===")
        print("Guess the number from 1-100!")


        random_number = random.randint(1, 100)
        tries = 10

        while True:
            if tries == 0:
                print("You lost!")
                loses += 1
                break
            print(f"You have {tries} tries")
            user_number = int(input("Guess the number: "))
            if user_number > 100:
                print("Invalid, your guess must be 1-100 only.")
                tries -= 1
                fake_tries -= 1
            elif user_number == random_number:
                print("You have guessed the number!")
                wins += 1
                break
            elif user_number > random_number:
                tries -= 1
                fake_tries -= 1
                print("Your guess is too high!")
            elif user_number < random_number:
                tries -= 1
                fake_tries -= 1
                print("Your guess is too low!")








while True:
    print("Welcome to Infinite Random Guessing Game")
    user_choice = input("Do you want to play? (y/n): ").strip().lower()

    if user_choice == 'y':
        fake_tries = 10
        Play.play()
    elif user_choice == 'n':
        print("You have exited the game.")
        Play.decision()
        print(f"You have {wins} win(s) and {loses} loses.")
        break
    else:
        print("Invalid.")
