# Import the service layer that handles transaction business logic
from services.transaction_service import TransactionService
from models.transaction import Transaction

# Controller class that handles transaction-related actions
class TransactionController:

    # Static method to add a new transaction to the database
    @staticmethod
    def add_transaction(transaction: Transaction):
        TransactionService.add(transaction)

    # Static method to delete all transactions from the database
    def clear_all_transactions():
        TransactionService.clear_all()