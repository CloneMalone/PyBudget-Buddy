# Import the service layer that handles summary/dashboard logic
from services.summary_service import SummaryService

# Controller class that handles summary/dashboard-related actions
class SummaryController:

    # Static method that fetches all transactions and formats them for display
    @staticmethod
    def get_all_transactions():

        # Pull all transactions from the database
        transactions = SummaryService.get_all_transactions()

        # If transactions exist, format them with nice display values
        if transactions:
            transactions_dict = [
                {
                    "id": row['id'],
                    "name": row['name'],
                    "amount": f"$ {row['amount']}",
                    "category": row['category'],
                    "date": f"{row['date']}",
                    "type": row['type'],
                }
                for row in transactions
            ]
        else:
            # Return empty list if no transactions exist
            return []

        return transactions_dict



    # Static method that gets total income and expenses
    @staticmethod
    def get_total_income_and_expenses():
        SummaryService.get_total_income_and_expenses()