#Kitchen System


class KitchenSystem:
    def __init__(self):
        self.queue = list()
        self.plates = list()

    def add_order(self, order):
        self.queue.append(order)
        print(f"{order} has been placed in the queue")

    def add_plates(self, plate):
        self.plates.append(plate)
        print("A plate has been added")

    def serve_dish(self):
        if len(self.queue) > 0 and len(self.plates) > 0:
            print(f"{self.queue.pop(0)} has been serve on a clean {self.plates.pop()}")
        elif len(self.queue) > 0 and len(self.plates) == 0:
            print(f"We have food but no plates! Clean more plates!")
        elif len(self.queue) == 0 and len(self.plates) > 0:
            print(f"No orders to cook.")
        else:
            print("No orders to cook.")


kitchen = KitchenSystem()
while True:
    user_input = input("(a) to add plates, (s) to serve dish, type anything to order: ")
    if user_input == 'a':
        kitchen.add_plates("plate")
    elif user_input == 's':
        kitchen.serve_dish()
    else:
        kitchen.add_order(user_input)