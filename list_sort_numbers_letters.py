#List cleaner

raw_list = []

print("Type (stop) to stop typing.")


def split():
    raw_list.remove('stop')
    number_list = [item for item in raw_list if item.isdigit()]
    letter_list = [letter for letter in raw_list if letter.isalpha()]
    print(f"NUMBER LIST: {number_list}")
    print(f"LETTER LIST: {letter_list}")


while True:

    user_input = input("Type any characters: ").strip()
    raw_list.append(user_input)

    if user_input == 'stop':
        split()
        break

