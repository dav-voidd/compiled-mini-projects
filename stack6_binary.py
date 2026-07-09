#Decimal to Binary Converter



class Binary:
    def __init__(self):
        self.binary = list()



    def push_remainder(self, value):

        while value > 0:
            new_value = value % 2
            self.binary.append(new_value)
            value = value // 2


    def pop(self):
        while self.binary:
            print(self.binary.pop(), end=" ")

    def see_binary(self):
        return self.binary


convert_number = Binary()

while True:
    user_input = int(input("\nPut number: "))
    convert_number.push_remainder(user_input)
    convert_number.pop()

