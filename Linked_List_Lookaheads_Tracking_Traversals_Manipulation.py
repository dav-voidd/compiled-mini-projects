#Tail Cutter

class Person:
    def __init__(self, name):
        self.name = name
        self.next = None

class TicketLine:
    def __init__(self):
        self.head = None

    def add_line(self, name):
        new_person_inline = Person(name)
        if self.head is None:
            self.head = new_person_inline
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_person_inline


    def remove_front(self):
        if self.head is None:
            print("No person in line!")
            return
        else:
            print(f"{self.head.name}'s ticket is now processed! next!")
            self.head = self.head.next

    def remove_back(self):
        if self.head is None:
            print("No one in line!")
            return
        if self.head.next is None:
            print("There's only 1 in line")
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        print(f"{current.next.name} is removed!")
        current.next = None

    def get_count(self):
        current = self.head
        count_people = 0
        while current is not None:
            count_people += 1
            current = current.next
        return f"{count_people}"

    def insert_at(self, index, name):
        new_person = Person(name)

        if index == 0:
            new_person.next = self.head
            self.head = new_person
            return

        current = self.head
        position = 0

        while current is not None and position < index - 1:
            current = current.next
            position += 1


        if current is None:
            print("Index out of bounds! Line isn't that long.")
            return

        new_person.next = current.next
        current.next = new_person

    def delete(self, target_name):
        if self.head is None:
            print("There is no one in line!")
            return
        if self.head.name == target_name:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.name == target_name:
                print(f"{current.next.name} has been removed.")
                current.next = current.next.next
                return
            current = current.next
        print(f"{target_name} is not on this line!")

    def reverse_line(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = prev
            prev = current

            current = next_node

        self.head = prev
        print("The line has been reversed!")

    def purge_duplicates(self):
        seen_names = set()
        if self.head is None:
            print("There is no one in line")
            return

        current = self.head
        seen_names.add(self.head.name)

        while current.next is not None:
            if current.next.name in seen_names:
                current.next = current.next.next
            else:
                seen_names.add(current.next.name)
                current = current.next





ticket = TicketLine()
while True:
    user_input = input("(u) to purge duplicates, (d) to delete person, (i) to to add vip, (p) to process a person, (b) to remove back, (c) to count how many, (r) to reverse line, Type to add person in line: ")
    if user_input == 'p':
        ticket.remove_front()
    elif user_input == 'b':
        ticket.remove_back()
    elif user_input == 'c':
        print(f"There are {ticket.get_count()} people in line!")
    elif user_input == 'i':
        user_name1 = input("Put VIP name: ")
        user_index = int(input("Put desired position/index: "))
        ticket.insert_at(user_index, user_name1)
    elif user_input == 'd':
        user_name2 = input("Add the specific name of the person you want to delete: ")
        ticket.delete(user_name2)
    elif user_input == 'r':
        ticket.reverse_line()
    elif user_input == 'u':
        ticket.purge_duplicates()
    else:
        ticket.add_line(user_input)
