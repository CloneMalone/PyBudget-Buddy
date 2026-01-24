import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

from frames.center import Center
from frames.button_group import ButtonGroup

from models.transaction import Transaction
from controllers.transaction_controller import TransactionController



class AddIncomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # We must place a frame within the current
        # view so that widgets can center properly
        center = Center(self)

        ttk.Label(center, text="Add Income", style="Header.TLabel").pack(pady=20)

        # For storing the input values
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.source_var = tk.StringVar()

        ttk.Label(center, text="Name", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.name_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        ttk.Label(center, text="Amount", style="Form.TLabel").pack(anchor="w")
        self.amount_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.amount_var)
        self.amount_entry.pack(pady=(4, 12), fill="x")

        ttk.Label(center, text="Source", style="Form.TLabel").pack(anchor="w")
        self.source_entry = ttk.Entry(center, 
                                      style="Form.TEntry", 
                                      textvariable=self.source_var)
        self.source_entry.pack(pady=(4, 20), fill="x")
        
        # This is for grouping the buttons horizontally
        button_group = ButtonGroup(center)

        ttk.Button(
            button_group,
            text="Save Income",
            style="Primary.TButton",
            command=lambda: self.add_income(parent)
        ).pack(side="left", padx=10)

        ttk.Button(
            button_group,
            text="Home",
            style="Primary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home") 
        ).pack(side="left", padx=10)


    def add_income(self, parent):
        # Grab the input values
        name = self.name_var.get()
        amount = round(float(self.amount_var.get()), 2)
        source = self.source_var.get()

        # Create a transaction object with both input data
        # and hardcoded dated that applies to all income transactions
        transaction = Transaction(name, amount, source, "Income")

        # Add transaction to database
        TransactionController.add_transaction(transaction)

        # Take user back to the dashboard
        parent.show_frame("dashboard", reason="income_added")


