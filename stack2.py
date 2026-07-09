class Browser:
    def __init__(self):
        self.stack = list()
    def visit_website(self, item):
        self.stack.append(item)

    def go_back(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        return "No more websites to close."

    def current(self):
        if len(self.stack) > 0:
            return f"{self.stack[-1]} - -is the current website you are in"
        else:
            return "No more websites."

    def __str__(self):
        return str(self.stack)


new_url = Browser()

while True:
    user_input = input("Type V to visit page or Type back to go back: ").strip().lower()


    if user_input == 'v':
        user_url = input("Visit Pages: ")
        new_url.visit_website(user_url)

        print(f"{new_url.current()}")

    elif user_input == "back":
        new_url.go_back()
        print(f"{new_url.current()}")


