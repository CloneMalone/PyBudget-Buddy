import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

from frames.center import Center
from frames.button_group import ButtonGroup

from models.transaction import Transaction
from controllers.transaction_controller import TransactionController

class AddExpenseView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        center = Center(self)

        # Variables for input fields
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()

        ttk.Label(center, text="Add Expense", style="Header.TLabel").pack(pady=20)

        # Name
        ttk.Label(center, text="Name", style="Form.TLabel").pack(anchor="w")
        self.name_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.name_var)
        self.name_entry.pack(pady=(4, 12), fill="x")

        # Amount
        ttk.Label(center, text="Amount", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.amount_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        # Category
        ttk.Label(center, text="Category", style="Form.TLabel").pack(anchor="w")
        self.category_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.category_var)
        self.category_entry.pack(pady=(4, 20), fill="x")

        # Button group
        button_group = ButtonGroup(center)

        ttk.Button(
            button_group,
            text="Save Expense",
            style="Primary.TButton",
            command=lambda: self.add_expense(parent)
        ).pack(side="left", padx=10)

        ttk.Button(
            button_group,
            text="Home",
            style="Primary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home") 
        ).pack(side="left", padx=10)

    def add_expense(self, parent):
        # Grab the input values
        name = self.name_var.get()
        amount = round(float(self.amount_var.get()), 2)
        category = self.category_var.get()

        # Create transaction object
        transaction = Transaction(name, amount, category, "Expense")

        # Add transaction to database
        TransactionController.add_transaction(transaction)

        # Go back to dashboard
        parent.show_frame("dashboard", reason="expense_added")
