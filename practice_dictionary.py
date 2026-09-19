#Personal Expense Tracker

def add_expense_to_list(expense_list, category, amount):
    expense_list = {
        "category": category,
        "amount": amount
    }
    return expense_list

my_expenses = []
my_expenses = add_expense_to_list(my_expenses, "Groceries", 17.38)
my_expenses = add_expense_to_list(my_expenses, "Gym", 20.0)
print(my_expenses)