from services.transaction_service import TransactionService
from models.transaction import Transaction

class TransactionController:

    @staticmethod
    def add_transaction(transaction: Transaction):
        TransactionService.add(transaction)

    def clear_all_transactions():
        TransactionService.clear_all()