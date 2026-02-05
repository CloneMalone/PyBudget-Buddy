# Import database connection utilities
from models.database import get_connection


# Service class that handles all summary/dashboard data operations
class SummaryService:

    # Static method that retrieves all transactions from the database
    @staticmethod
    def get_all_transactions():
        # Print blank line for console breathing room
        print("")

        conn = get_connection()
        cursor = conn.cursor()

        # SQL statement for pulling all transactions (newest first)
        statement = "SELECT * FROM transactions ORDER BY date DESC, id DESC"

        # Execute the query
        cursor.execute(statement)

        # Print the statement that just ran
        # Log what just ran
        print("🧾 SQL EXECUTED:")
        print(statement)
        

        # Grab all rows from the result
        rows = cursor.fetchall()
        print("➡️   VALUES:")
        print(*rows, sep='\n')
        

        conn.close()

        # Convert raw rows into friendly dictionaries
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


    # Static method that calculates total income and expenses
    @staticmethod
    def get_total_income_and_expenses():
        # Print blank line for console spacing
        print("")

        conn = get_connection()
        cursor = conn.cursor()

        # SQL statement for grabbing amounts and types
        statement = "SELECT amount, type FROM transactions"

        # Execute the query
        cursor.execute(statement)

        # Print the statement that just ran
        print(statement)

        rows = cursor.fetchall()

        # Running totals
        total_income = 0
        total_expenses = 0

        # Add amounts to the correct bucket
        for amount, txn_type in rows:
            if txn_type.lower() == "income":
                total_income += amount
            elif txn_type.lower() == "expense":
                total_expenses += amount

        conn.close()

        # Return totals in a clean, readable shape
        return {
            "total_income": total_income,
            "total_expenses": total_expenses
        }
