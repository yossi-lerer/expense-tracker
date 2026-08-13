import time

def calculate_total(expenses: list):
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
    return total_amount

def show_expenses(expenses: list):
    for expense in expenses:
        print("\n")
        for feild in expense:
            print(f"{feild}: {expense[feild]}")
    print(f"total amount: {calculate_total(expenses)}")

def add_expense(expenses: list, title: str, category: str, amount: float):
    expenses.append({'data': time.strftime("%Y-%m-%d"), 'title': title, 'category': category, 'amount': amount})

def ask_for_expense(expenses: list):
    title = input("Enter the name of the expense. ")
    category = input("Enter the category. ")
    try:
        amount = float(input("Enter the expense amount. "))
    except:
        return False
    add_expense(expenses, title, category, amount)

def manager_flow(expenses):
    show_expenses(expenses)
    ask_more_expense = True
    while ask_more_expense:
        ask_expense = input("Do you want to add another expense? 1 for 2 for No ")
        if ask_expense == "1":
            if ask_for_expense(expenses) != False:
                show_expenses(expenses)
            else:
                print("The expense was not recorded, only numbers must be entered in the amount.")
        else:
            ask_more_expense = False