from services.summary_service import SummaryService

class SummaryController:

    @staticmethod
    def get_all_transactions():

        # Pull all transactions from the database
        transactions = SummaryService.get_all_transactions()

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
            return []

        return transactions_dict



    @staticmethod
    def get_total_income_and_expenses():
        SummaryService.get_total_income_and_expenses()