#The Undoable Inventory System


class Inventory:
    def __init__(self):
        self.inventory = list()

    def pick_up(self, item):
        self.inventory.append(item)
        print(f"You just picked! {self.inventory[-1]}")

    def thief(self):
        print(f"A thief stole your {self.inventory.pop()} !")

bag = Inventory()
while True:
    user_input = input("Pick up weapons! Type (s) for Sword, (S) for Shield: ")
    if user_input == 's':
        s = 'Sword'
        bag.pick_up(s)
    elif user_input == 'S':
        S = 'Shield'
        bag.pick_up(S)
    else:
        bag.thief()
