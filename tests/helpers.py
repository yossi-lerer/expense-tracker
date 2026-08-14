def total(expenses: list):
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
    return total_amount

def total_by_category(expenses: list) -> dict:
    expense_category = {}
    for expense in expenses:
        if expense['category'] in expense_category:
            expense_category[expense['category']] += expense['amount']
        else:
            expense_category[expense['category']] = expense['amount']
    return expense_category