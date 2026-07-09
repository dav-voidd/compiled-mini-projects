class Math:
    def __init__(self):
        self.parenthesis = list()

    def check_balance(self, equation):
        for char in equation:
            if char == '(':
                self.parenthesis.append(char)
            elif char == ')':
                if self.parenthesis:
                    self.parenthesis.pop()
                else:
                    print("Not Balanced! (Too many closing brackets)")


        if len(self.parenthesis) == 0:
            print("Perfectly Balanced!")
        else:
            print("Not Balanced! (Too many opening brackets)")



    def peek(self):
        return self.parenthesis

test = Math()
test.check_balance('((5x + 1) + )1)')

print(test.peek())