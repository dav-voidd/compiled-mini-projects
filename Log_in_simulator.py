#Log In Simulator

accounts = {}



class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        accounts[self.name] = self.password


def new_account():
        user_name = input("Enter the desired user: ").strip().title()
        user_password = input("Enter the desired password: ").strip()
        new_accounts = Account(user_name, user_password)
        return new_accounts


def check():
        login_user_name = input("Username: ").strip().title()
        login_password = input("Password: ").strip()
        if login_user_name in accounts:
            if accounts[login_user_name] == login_password:
                print("Logged Successfully!")
            elif accounts[login_user_name] != login_password:
                print("Invalid Password")
        elif login_user_name not in accounts:
            print("Invalid Username")


while True:
    user_create = input("Do you want to create an account? (y/n): ").strip().lower()
    if user_create == 'y':
        new_account()
    elif user_create == 'n':
        user_choice = input("Do you want to log-in? (y/n): ").strip().lower()
        if user_choice == 'y':
            check()
        elif user_choice == 'n':
            print("You have exited.")
            break
    else:
        break





