#Password Inspector

while True:

    user_password = input("Whats your password: ").strip()
    length = len(user_password)

    def has_numbers(password):
        return any(char.isdigit() for char in password)


    if length >= 10 and has_numbers(user_password) is True:
        print("valid password.")

    elif length >= 10 and has_numbers(user_password) is False:
        print("Password must contain numbers.")

    elif length < 10 and has_numbers(user_password) is True:
        print("Password must have greater or equal to 10 characters.")

    elif length < 10 and has_numbers(user_password) is False:
        print("Password must be greater or equal to 10 and contains at least 1 number.")



