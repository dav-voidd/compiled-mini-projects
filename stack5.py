#Country Visit Log


class Travel:

    def __init__(self):
        self.visited = list()

    def new_country(self, country):
        self.visited.append(country)

    def total_countries(self):
        return len(self.visited)


    def last_visit(self):
        return self.visited[-1]


new_travel = Travel()

while True:
    user_input = input("(t) for total visits, (l) for last visits, Type country: ")
    if user_input == 't':
        print(f"{new_travel.total_countries()} number of total countries you visited.")
    elif user_input == 'l':
        print(f"{new_travel.last_visit()} is the last country you visited.")
    else:
        new_travel.new_country(user_input)

