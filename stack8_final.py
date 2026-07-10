#Limited-Capacity Stack


class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, name):
        if len(self.stack) < 5:
            self.stack.append(name)
        elif len(self.stack) == 5:
            print("Stack overflow!")


    def count(self):
        return self.stack

    def __str__(self):
        return str(self.stack)

obj = Stack()
while True:
        user_input = input("Put item: ")
        obj.push(user_input)
        print(obj.count())
