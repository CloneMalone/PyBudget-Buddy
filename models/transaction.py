from datetime import date

class Transaction:
    def __init__(self, name, amount, category, _type):
        self.name = name
        self.amount = amount
        self.category = category
        self._date = date.today()
        self._type = _type

    @property
    def date(self):
        return self._date.strftime("%m/%d/%Y")
