# What is this project 
expense tracker:
The program saves your expenses (money you spent) in a file, and shows them in a nice table.

# Installation
git clone https://github.com/yossi-lerer/expense-tracker
cd expense-tracker
Create an .env file like .env.example
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# How to use
python main.py
python main.py add "Coffee" food 12
python main.py list
python main.py report
pytest

# Settings
in env file you can change the currency and budget

# The 5 packages
rich https://rich.readthedocs.io/en/stable/introduction.html show a beautiful table
questionary https://questionary.readthedocs.io/ improve the user input 
typer https://typer.tiangolo.com/tutorial/first-steps/ turn it into a real command line tool
python-dotenv https://pypi.org/project/python-dotenv/ settings in a .env file
pytest https://docs.pytest.org/en/stable/getting-started.html test the code

