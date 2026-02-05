# Import the service layer that handles summary/dashboard logic
from services.summary_service import SummaryService


# Controller class that handles summary/dashboard-related actions
class SummaryController:

    # Static method that fetches all transactions and formats them for display
    @staticmethod
    def get_all_transactions():
        # Pull all transactions from the database
        transactions = SummaryService.get_all_transactions()

        # Return early if nothing exists
        if not transactions:
            return []

        # Format transactions for display
        formatted_transactions = []

        for row in transactions:
            formatted_transactions.append(
                {
                    "id": row["id"],
                    "name": row["name"],
                    "amount": f"$ {row['amount']:.2f}",
                    "category": row["category"],
                    "date": row["date"],
                    "type": row["type"],
                }
            )

        return formatted_transactions

    # Static method that returns formatted totals
    @staticmethod
    def get_total_income_and_expenses():
        totals = SummaryService.get_total_income_and_expenses()

        return {
            "income": f"$ {totals['total_income']:.2f}",
            "expenses": f"$ {totals['total_expenses']:.2f}",
        }

    # Static method that returns expense-only data
    @staticmethod
    def get_expenses_summary():
        transactions = SummaryService.get_all_transactions()

        expenses = []
        total = 0.00

        for txn in transactions:
            if txn["type"].lower() == "expense":
                expenses.append(txn)
                total += txn["amount"]

        return {
            "total": f"$ {total:.2f}",
            "rows": expenses,
        }

    # Static method that returns income-only data
    @staticmethod
    def get_income_summary():
        transactions = SummaryService.get_all_transactions()

        income = []
        total = 0.00

        for txn in transactions:
            if txn["type"].lower() == "income":
                income.append(txn)
                total += txn["amount"]

        return {
            "total": f"$ {total:.2f}",
            "rows": income,
        }
