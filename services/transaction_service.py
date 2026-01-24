# Import database connection utilities and Transaction model
from models.database import get_connection
from models.transaction import Transaction


# Service class that handles all transaction database operations
class TransactionService:

    # Static method that inserts a new transaction into the database
    @staticmethod
    def add(transaction: Transaction):
        conn = get_connection()
        cursor = conn.cursor()

        # Insert the transaction's data into the transactions table
        cursor.execute(
            """
            INSERT INTO transactions (name, amount, category, date, type)
            VALUES (?, ?, ?, ?, ?)


""",
            (
                transaction.name,
                transaction.amount,
                transaction.category,
                transaction._date,
                transaction._type,
            ),
        )

        # Save changes to the database and close the connection
        conn.commit()
        conn.close()

    # Static method that deletes all transactions from the database
    @staticmethod
    def clear_all():
        conn = get_connection()
        cursor = conn.cursor()

        # Delete all rows from the transactions table
        cursor.execute("DELETE FROM transactions")

        # Save changes and close the connection
        conn.commit()
        conn.close()

