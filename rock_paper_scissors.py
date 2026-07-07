#Rock, Paper, Scissors, Shoot!
import random



class Play:
    wins = 0
    loses = 0

    def play():

        random_choice = random.randint(1, 3)
        print("=== Rock, Paper, Scissors Shoot! ===")
        user_choice = input("Type (R) Rock, (P) Paper, (S) Scissors to shoot: ").upper()
        if user_choice == 'R':
            value = 1
            if value == random_choice:
                print("Draw")
            elif random_choice == 2:
                print("You have lost. Computer chose Paper")
                Play.loses += 1
            elif random_choice == 3:
                print("You won! You chose Rock and Computer chose Scissors")
                Play.wins += 1
        elif user_choice == 'P':
            value = 2
            if value == random_choice:
                print("Draw")
            elif random_choice == 3:
                print("You have lost. Computer chose Scissors")
                Play.loses += 1
            elif random_choice == 1:
                print("You won! You chose Paper and Computer chose Rock")
                Play.wins += 1
        elif user_choice == 'S':
            value = 3
            if value == random_choice:
                print("Draw")
            elif random_choice == 2:
                print("You won! You chose Scissors and Computer chose Paper")
                Play.wins += 1
            elif random_choice == 1:
                print("You lost! Computer chose Rock")
                Play.loses += 1


while True:
    print("Welcome to Rock, Paper, Scissors Shoot Game!")
    user_want = input("Do you want to play? (y/n): ").strip().lower()

    if user_want == 'y':
        Play.play()
    elif user_want == 'n':
        print("You have exited the game.")
        print(f"You have {Play.wins} win(s) and {Play.loses} loses.")
        break
    else:
        print("Invalid.")
