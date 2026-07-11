



class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

    def __str__(self):
        return self.queue



test = Queue()
while True:
    user_input = input("Put an item: ")
    if user_input == 'd':
        test.dequeue()
        print(f"{test.queue}")
    else:
        test.enqueue(user_input)
        print(f"{test.queue}")