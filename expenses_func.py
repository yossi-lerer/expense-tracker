import time
from rich.console import Console
from rich.table import Table
import questionary
import config

def calculate_total(expenses: list):
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
    return total_amount

def show_expenses(expenses: list):
    table = Table(title="expenses")
    table.add_column("data", justify="left", style="cyan")
    table.add_column("title", justify="left", style="green")
    table.add_column("category", justify="left", style="green")
    table.add_column("amount", justify="left", style="green")
  
    for expense in expenses:
        table.add_row(expense['data'], expense['title'], expense['category'], str(expense['amount']) + " " + config.currency)
    console = Console()
    console.print(table)
    console.print(f"total amount: {calculate_total(expenses):.2f} {config.currency}", style="magenta")

def add_expense(expenses: list, title: str, category: str, amount: float):
    expenses.append({'data': time.strftime("%Y-%m-%d"), 'title': title, 'category': category, 'amount': amount})

def ask_for_expense(expenses: list):
    title = questionary.text("Enter the name of the expense").ask()
    category = questionary.select(
    "Enter the category?",
    choices=[
        "food",
        "travel",
        "school",
        "entertainment",
        "other"
    ]).ask()
    try:
        amount = float(questionary.text("Enter the expense amount").ask())
    except:
        return False
    add_expense(expenses, title, category, amount)

def manager_flow(expenses):
    show_expenses(expenses)
    ask_more_expense = True
    while ask_more_expense:
        ask_expense =questionary.select("Do you want to add another expense? 1 for 2 for No", choices=[
        "1",
        "2"
    ]).ask()
        if ask_expense == "1":
            if ask_for_expense(expenses) != False:
                show_expenses(expenses)
            else:
                print("The expense was not recorded, only numbers must be entered in the amount.")
        else:
            ask_more_expense = False