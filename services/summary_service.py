# Import database connection utilities
from models.database import get_connection

# Service class that handles all summary/dashboard data operations
class SummaryService:

    # Static method that retrieves all transactions from the database in reverse order
    @staticmethod
    def get_all_transactions():
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch all transactions ordered by date (newest first), then by ID
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC, id DESC")
        rows = cursor.fetchall()
        conn.close()
        
        # Convert raw database rows into a list of dictionaries for easier access
        transactions = [
            {
                "id": row[0],
                "name": row[1],
                "amount": row[2],
                "category": row[3],
                "date": row[4],
                "type": row[5],
            }
            for row in rows
        ]

        return transactions


    # Static method that calculates total income and total expenses
    @staticmethod
    def get_total_income_and_expenses():
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch all transactions with their amounts and types
        cursor.execute("SELECT amount, type FROM transactions")
        rows = cursor.fetchall()

        # Initialize counters for income and expenses
        total_income = 0
        total_expenses = 0

        # Loop through each transaction and add to appropriate total
        for amount, txn_type in rows:
            if txn_type.lower() == "income":
                total_income += amount
            elif txn_type.lower() == "expense":
                total_expenses += amount

        conn.close()

        # Return the totals as a dictionary
        return {
            total_income,
            total_expenses
        }

