# Import database connection utilities and Transaction model
from models.database import get_connection
from models.transaction import Transaction


# Service class that handles all transaction database operations
class TransactionService:

    # Static method that inserts a new transaction into the database
    @staticmethod
    def add(transaction: Transaction):
        # Print blank line
        print("")

        conn = get_connection()
        cursor = conn.cursor()

        # Create statement
        statement = """
        INSERT INTO transactions (name, amount, category, date, type)
        VALUES (?, ?, ?, ?, ?)
        """

        # Identify values to be added
        values = (
            transaction.name,
            transaction.amount,
            transaction.category,
            transaction._date,
            transaction._type,
        )

        # Insert the transaction's data into the transactions table
        cursor.execute(statement, values)

        # Log what just ran
        print("🧾 SQL EXECUTED:")
        print(statement.strip())
        print("➡️ VALUES:", values)

        # Save changes to the database and close the connection
        conn.commit()
        conn.close()

    # Static method that deletes all transactions from the database
    @staticmethod
    def clear_all():
        # Print blank line
        print("")

        conn = get_connection()
        cursor = conn.cursor()

        statement = "DELETE FROM transactions"
        print(statement)

        # Delete all rows from the transactions table
        cursor.execute(statement)

        # Save changes and close the connection
        conn.commit()
        conn.close()

