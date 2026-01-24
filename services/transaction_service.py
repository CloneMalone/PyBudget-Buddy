from models.database import get_connection
from models.transaction import Transaction


class TransactionService:

    @staticmethod
    def add(transaction: Transaction):
        conn = get_connection()
        cursor = conn.cursor()

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

        conn.commit()
        conn.close()

    @staticmethod
    def clear_all():
        conn = get_connection()
        cursor = conn.cursor()

        # Delete all rows from the transactions table
        cursor.execute("DELETE FROM transactions")

        conn.commit()
        conn.close()

