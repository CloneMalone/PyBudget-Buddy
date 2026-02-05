# Import tkinter libraries for building the UI
import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

# Import custom frame components
from frames.center import Center
from frames.button_group import ButtonGroup

# Import the data model and controller
from models.transaction import Transaction
from controllers.transaction_controller import TransactionController

# View screen for adding new expense transactions
class AddExpenseView(ttk.Frame):
    # Initialize the Add Expense screen with form fields
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Create a centered frame for better layout
        center = Center(self)

        # Create StringVar variables to store the input values from form fields
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar()

        # Add the "Add Expense" header label
        ttk.Label(center, text="Add Expense", style="Header.TLabel").pack(pady=20)

        # Create label and entry field for the name/description of the expense
        ttk.Label(center, text="Name", style="Form.TLabel").pack(anchor="w")
        self.name_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.name_var)
        self.name_entry.pack(pady=(4, 12), fill="x")

        # Create label and entry field for the amount of the expense
        ttk.Label(center, text="Amount", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.amount_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        # Create label and entry field for the category of the expense
        ttk.Label(center, text="Category", style="Form.TLabel").pack(anchor="w")
        self.category_entry = ttk.Entry(center, style="Form.TEntry", textvariable=self.category_var)
        self.category_entry.pack(pady=(4, 20), fill="x")

        # Create a button group to hold the action buttons horizontally
        button_group = ButtonGroup(center)

        # Button to save the expense and return to dashboard
        ttk.Button(
            button_group,
            text="Save Expense",
            style="Primary.TButton",
            command=lambda: self.add_expense(parent)
        ).pack(side="left", padx=10)

        # Button to return to dashboard without saving
        ttk.Button(
            button_group,
            text="Home",
            style="Secondary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home") 
        ).pack(side="left", padx=10)

    # Method to handle saving the expense entry
    def add_expense(self, parent):
        # Grab the input values from the form fields
        name = self.name_var.get()
        amount = round(float(self.amount_var.get()), 2)
        category = self.category_var.get()

        # Create transaction object with the form data
        # and the type set to "Expense" (date is automatically set to today)
        transaction = Transaction(name, amount, category, "Expense")

        # Add transaction to database via the controller
        TransactionController.add_transaction(transaction)

        # Go back to the dashboard and trigger the expense_added callback
        parent.show_frame("dashboard", reason="expense_added")

