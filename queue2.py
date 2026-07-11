#Stack + Queues
#The Palindrome checker


class PalindromeChecker:
    def __init__(self):
        self.queue = list()
        self.stack = list()

    def check(self, word):
        for i in word:
            self.queue.append(i)
            self.stack.append(i)


        for i in range(len(self.stack)):
            if self.stack.pop() != self.queue.pop(0):
                return "Not palindrome"
        return "Palindrome"


test = 'nigger'
palindrome = PalindromeChecker()
print(f"{palindrome.check(test)}")



