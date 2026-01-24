import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

from frames.center import Center
from frames.button_group import ButtonGroup
from components.tree_view import TreeView

from controllers.summary_controller import SummaryController
from controllers.transaction_controller import TransactionController


class DashboardView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Center frame
        self.center = Center(self)

        # Header
        ttk.Label(
            self.center,
            text="Dashboard",
            style="Header.TLabel"
        ).pack(pady=20)

        # Buttons
        button_group = ButtonGroup(self.center)

        ttk.Button(
            button_group,
            text="Add Income",
            style="Primary.TButton",
            command=lambda: parent.show_frame("add_income")
        ).pack(side="left", padx=10)

        ttk.Button(
            button_group,
            text="Add Expense",
            style="Primary.TButton",
            command=lambda: parent.show_frame("add_expense")
        ).pack(side="left", padx=10)

        ttk.Button(
            button_group,
            text="Clear All Transactions",
            style="Danger.TButton",
            command=self.clear_all_transactions
        ).pack(side="left", padx=10)

        # Labels
        self.loading_label = ttk.Label(
            self.center,
            text="Loading transactions...",
            style="Loading.TLabel"
        )
        self.message_label = ttk.Label(
            self.center,
            text="",
            style="Loading.TLabel"
        )

        # Transaction table
        self.transaction_table = TreeView(
            self.center,
            columns=("name", "amount", "category", "date", "type"),
            headings={
                "name": "📝 Name",
                "amount": "💲 Amount",
                "category": "📕 Category",
                "date": "📅 Date",
                "type": "💰 Type"
            }
        )

    def clear_all_transactions(self):
        # Hide previous message
        self.message_label.pack_forget()

        transactions = SummaryController.get_all_transactions() or []

        if not transactions:
            self.show_message("❌ Unable to clear transactions. None exist.")
        else:
            self.show_message("🗑️ Clearing transactions...")
            TransactionController.clear_all_transactions()
            self.after(800, lambda: self.load_transactions(reason="cleared"))

    def show_message(self, text, duration=1500):
        """Show a temporary label in the center."""
        self.message_label.config(text=text)
        self.message_label.pack(pady=10)
        # Hide automatically after duration
        self.after(duration, self.message_label.pack_forget)

    def load_transactions(self, reason="default"):
        # Hide any previous message
        self.message_label.pack_forget()

        # Show appropriate loading or feedback
        if reason == "first_load":
            self.loading_label.config(text="Loading transactions...")
            self.loading_label.pack(pady=20)
        elif reason == "income_added":
            self.loading_label.config(text="💲 Adding Income...")
            self.loading_label.pack(pady=20)
        elif reason == "expense_added":
            self.loading_label.config(text="💰 Adding Expense...")
            self.loading_label.pack(pady=20)
        elif reason == "cleared":
            self.loading_label.config(text="Refreshing transactions...")
            self.loading_label.pack(pady=20)
        else:
            self.loading_label.config(text="Refreshing transactions...")
            self.loading_label.pack(pady=20)

        # Schedule actual data load
        self.after(800, self.finish_loading)

    def finish_loading(self):
        transactions = SummaryController.get_all_transactions() or []

        rows = [
            (t["name"], t["amount"], t["category"], t["date"], t["type"])
            for t in transactions
        ]

        self.transaction_table.clear()
        self.transaction_table.load_data(rows)

        # Remove loading label
        self.loading_label.pack_forget()

        # Pack table now that it has data
        self.transaction_table.pack(pady=10, fill="x")

    # Use this on first app load
    def on_show_first_load(self):
        self.load_transactions(reason="first_load")

    # Use this when returning from Add Income
    def on_show_after_income(self):
        self.load_transactions(reason="income_added")

    # Use this when returning from Add Expense
    def on_show_after_expense(self):
        self.load_transactions(reason="expense_added")

    # Use this for normal home navigation
    def on_show_home(self):
        self.load_transactions(reason="default")
