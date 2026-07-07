#Digital Rolodex



class Contacts:
    contacts = {}

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Contacts.contacts[self.name] = self.number


    @classmethod
    def search_contacts(cls):
        user_input = input("Put the name: ").title()
        if user_input in cls.contacts:
            print(f"{user_input} | No. {cls.contacts.get(user_input)}")
        else:
            print(f"There is no {user_input} name in the list.")

    @classmethod
    def delete_contacts(cls):
        if not Contacts.contacts:
            print("There's no names yet.")
        else:
            for i in Contacts.contacts:
                print(i)
            user_choice = input("What's the name: ").title()
            if user_choice in cls.contacts:
                cls.contacts.pop(user_choice)
                print(f"{user_choice} has been removed.")




while True:
    print("Welcome to your Contact's List")
    user_input1 = input("Type (A) to add contacts, Type (S) to search contacts, Type (D) to delete contacts or Press Enter to Quit: ").lower().strip()
    if user_input1 == 'a':
        new_name = input("Name: ").title()
        new_number = input("Number: ")
        new_contact = Contacts(new_name, new_number)
    elif user_input1 == 's':
        Contacts.search_contacts()
    elif user_input1 == 'd':
        Contacts.delete_contacts()
    elif user_input1 == '':
        break
    else:
        print("Invalid.")