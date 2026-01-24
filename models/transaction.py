# Import date functionality to automatically set transaction dates
from datetime import date

# This class represents a single transaction (income or expense)
class Transaction:
    # Initialize a transaction with name, amount, category, and type (Income or Expense)
    def __init__(self, name, amount, category, _type):
        self.name = name
        self.amount = amount
        self.category = category
        self._date = date.today()
        self._type = _type

    # Property that formats the date as a readable string (MM/DD/YYYY format)
    @property
    def date(self):
        return self._date.strftime("%m/%d/%Y")
