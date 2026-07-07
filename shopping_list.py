#Shopping List

shopping_list = []
print("Welcome to your Shopping List")
print("Type any items you want to add to your list. Type (V) to view list, Type (C) to clear list.")


while True:
    user_input = input("Type here: ").strip().lower()

    if user_input != 'v' and user_input != 'c':
        shopping_list.append(user_input.title())

    elif user_input == 'v':

        print("Shopping List")
        for i in range(len(shopping_list)):
            print(f"{i}. {shopping_list[i]}")

    elif user_input == 'c':
        shopping_list.clear()
        print("The list is now empty.")

    else:
        print("Invalid.")
