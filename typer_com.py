import typer
from data import expenses
from expenses_func import add_expense, show_expenses
app = typer.Typer()

@app.command()
def add(title: str, category: str, amount: float):
    add_expense(expenses, title, category, amount)
    show_expenses(expenses)

@app.command("list")
def list_items():
    show_expenses(expenses)