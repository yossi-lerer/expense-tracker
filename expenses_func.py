def show_expenses(expenses: list):
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
        print("\n")
        for feild in expense:
            print(f"{feild}: {expense[feild]}")
    print(f"\ntotal amount: {total_amount}")