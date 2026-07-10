#Limited-Capacity Stack


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, name):
        self.stack.append(name)

    def count(self):
        return self.stack

    def __str__(self):
        return str(self.stack)

obj = Stack()

while True:
    if len(obj.count()) < 5:
        user_input = input("Put item: ")
        obj.push(user_input)
        print(obj.stack)
    elif len(obj.count()) == 5:
        user_input = input("Put item: ")
        print("Stack overflow! Cannot add more items.")
    else:
        pass

