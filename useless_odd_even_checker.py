# Ultimate Odd and Even Checker

def checker():
    user_input = float(input("Type a number: "))
    if user_input % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd!")

checker()