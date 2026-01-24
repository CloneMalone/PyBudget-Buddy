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



# View screen for adding new income transactions
class AddIncomeView(ttk.Frame):
    # Initialize the Add Income screen with form fields
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Create a centered frame for better layout
        # (We must place a frame within the current view so that widgets can center properly)
        center = Center(self)

        # Add the "Add Income" header label
        ttk.Label(center, text="Add Income", style="Header.TLabel").pack(pady=20)

        # Create StringVar variables to store the input values from form fields
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.source_var = tk.StringVar()

        # Create label and entry field for the name of the income
        ttk.Label(center, text="Name", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.name_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        # Create label and entry field for the amount of the income
        ttk.Label(center, text="Amount", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.amount_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        # Create label and entry field for the source of the income
        ttk.Label(center, text="Source", style="Form.TLabel").pack(anchor="w")
        self.source_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.source_var)
        self.source_entry.pack(pady=(4, 20), fill="x")
        
        # Create a button group to hold the action buttons horizontally
        button_group = ButtonGroup(center)

        # Button to save the income and return to dashboard
        ttk.Button(
            button_group,
            text="Save Income",
            style="Primary.TButton",
            command=lambda: self.add_income(parent)
        ).pack(side="left", padx=10)

        # Button to return to dashboard without saving
        ttk.Button(
            button_group,
            text="Home",
            style="Primary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home") 
        ).pack(side="left", padx=10)


    # Method to handle saving the income entry
    def add_income(self, parent):
        # Grab the input values from the form fields
        name = self.name_var.get()
        amount = round(float(self.amount_var.get()), 2)
        source = self.source_var.get()

        # Create a transaction object with both input data
        # and the type set to "Income" (date is automatically set to today)
        transaction = Transaction(name, amount, source, "Income")

        # Add transaction to database via the controller
        TransactionController.add_transaction(transaction)

        # Take user back to the dashboard and trigger the income_added callback
        parent.show_frame("dashboard", reason="income_added")



