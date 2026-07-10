#Limited-Capacity Stack


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, name):
        if len(self.stack) < 5:
            self.stack.append(name)
            print(f"{self.stack}")
        elif len(self.stack) == 5:
            print("Stack overflow!")


obj = Stack()
while True:
        user_input = input("Put item: ")
        obj.push(user_input)

