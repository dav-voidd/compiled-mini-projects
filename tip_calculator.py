#Tip_Calculator


# The Tip Calculator


def calculate_split_bill():
    bill = float(input("Bill: "))
    tip = float(input("Tip Percentage: "))
    people = float(input("How many people: "))
    total_bill = bill * (1 + tip / 100)
    split_total_bill = total_bill / people
    print(f"The Total Bill is: {total_bill} \nEvery person will pay: {split_total_bill} each.")

calculate_split_bill()