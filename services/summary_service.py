from models.database import get_connection

class SummaryService:

    @staticmethod
    def get_all_transactions():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM transactions ORDER BY date DESC, id DESC")
        rows = cursor.fetchall()
        conn.close()
        
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


    @staticmethod
    def get_total_income_and_expenses():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT amount, type FROM transactions")
        rows = cursor.fetchall()

        total_income = 0
        total_expenses = 0

        for amount, txn_type in rows:
            if txn_type.lower() == "income":
                total_income += amount
            elif txn_type.lower() == "expense":
                total_expenses += amount

        conn.close()

        return {
            total_income,
            total_expenses
        }
