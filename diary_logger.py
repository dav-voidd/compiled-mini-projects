#Diary Logger


class Diary:
    def __init__(self, diary, date):
        self.diary = diary
        self.date = date
        with open("diary.txt", "a") as file:
            file.write(f"\n\n{self.date}: \n{self.diary}")

    @classmethod
    def clear(cls):
        with open("diary.txt", "w") as file:
            pass


print("=== DIARY ===")
while True:
    user_choice = input("Type Y to add, N to clear or ENTER to quit. (y/n): ").lower().strip()
    if user_choice == 'y':
        user_date = input("Type the date: ")
        user_diary = input("Type anything: ")
        new_diary = Diary(user_diary, user_date)
    elif user_choice == 'n':
        Diary.clear()
    elif user_choice == '':
        break
    else:
        print("Invalid")

