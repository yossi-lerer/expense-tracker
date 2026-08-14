import sys
from data import expenses
from expenses_func import manager_flow
from typer_com import app

def main():
    if len(sys.argv) == 1:
        manager_flow(expenses)
    else:
        app()

main()