#Ticketing Line


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

ticket = TicketLine()
while True:
    user_input = input("(p) to process a person, Type to add person in line: ")
    if user_input == 'p':
        ticket.remove_front()
    else:
        ticket.add_line(user_input)
