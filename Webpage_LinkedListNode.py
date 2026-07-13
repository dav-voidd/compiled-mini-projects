#Webpage Node


class PageNode:
    def __init__(self, url):
        self.url  = url
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self):
        self.current_page = None

    def visit_page(self, url):
        new_page = PageNode(url)
        if self.current_page is None:
            self.current_page = new_page
            print(f"Visited: {self.current_page.url}")
            return

        self.current_page.next = new_page
        new_page.prev = self.current_page
        self.current_page = new_page
        print(f"Visited: {self.current_page.url}")

    def go_back(self):
        if self.current_page.prev is not None:
            self.current_page = self.current_page.prev
            print(f"{self.current_page.url}")
        else:
            print("No previous page")


Web = BrowserHistory()
while True:
    user_input = input("(g) go back, Type to Add and visit a URL: ")
    if user_input == 'g':
        Web.go_back()
    else:
        Web.visit_page(user_input)





