import os
from dotenv import load_dotenv
load_dotenv()

currency = os.getenv("CURRENCY")
budget = os.getenv("MONTHLY_BUDGET")
