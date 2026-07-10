#Call Stack Simulator
#First create a class
#Create a stack
#Create a push function where it main() is called, "main" will be pushed and if main() calls calcualte(), "calculate" will also be pushed
# and when calculate is finished, it will pop everything
#So if main() true?
#We will use main() if statements

class Tracker:
    def __init__(self):
        self.stack = list()

    def push(self, name):
        self.stack.append(name)

    def pop(self):
        while self.stack:
            print(f"{self.stack.pop()}")



tracker = Tracker()
def main():
    tracker.push("main")
    calculate()

def calculate():
    tracker.push("calculate")
    tracker.pop()


main()










