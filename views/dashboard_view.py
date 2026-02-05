# Import tkinter libraries for building the UI
import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

# Import custom frame components
from frames.center import Center
from frames.button_group import ButtonGroup
from components.tree_view import TreeView

# Import controllers to handle business logic
from controllers.summary_controller import SummaryController
from controllers.transaction_controller import TransactionController


# Dashboard view that displays transactions and provides navigation buttons
class DashboardView(ttk.Frame):
    # Initialize the dashboard with all UI elements
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Create a centered frame for better layout
        self.center = Center(self)

        # Add the "Dashboard" header label
        ttk.Label(
            self.center,
            text="Dashboard",
            style="Header.TLabel"
        ).pack(pady=20)

        # Create a group for action buttons
        button_group = ButtonGroup(self.center)

        # Button to navigate to the Add Income screen
        ttk.Button(
            button_group,
            text="Add Income",
            style="Primary.TButton",
            command=lambda: parent.show_frame("add_income")
        ).pack(side="left", padx=10)

        # Button to navigate to the Add Expense screen
        ttk.Button(
            button_group,
            text="Add Expense",
            style="Primary.TButton",
            command=lambda: parent.show_frame("add_expense")
        ).pack(side="left", padx=10)

        # Button to navigate to the Expenses screen
        ttk.Button(
            button_group,
            text="View Expenses",
            style="Info.TButton",
            command=lambda: parent.show_frame("expenses", reason="home")
        ).pack(side="left", padx=10)

        # Button to navigate to the Income screen
        ttk.Button(
            button_group,
            text="View Income",
            style="Info.TButton",
            command=lambda: parent.show_frame("income", reason="home")
        ).pack(side="left", padx=10)

        # Button to delete all transactions (with danger styling)
        ttk.Button(
            button_group,
            text="Clear All Transactions",
            style="Danger.TButton",
            command=self.clear_all_transactions
        ).pack(side="left", padx=10)

        # Label that shows loading status
        self.loading_label = ttk.Label(
            self.center,
            text="Loading transactions...",
            style="Loading.TLabel"
        )
        # Label that shows temporary messages (success/error)
        self.message_label = ttk.Label(
            self.center,
            text="",
            style="Loading.TLabel"
        )

        # Create a table to display transactions
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

    # Method to clear all transactions with confirmation feedback
    def clear_all_transactions(self):
        # Hide any previous message label
        self.message_label.pack_forget()

        # Check if there are any transactions to clear
        transactions = SummaryController.get_all_transactions() or []

        # Show appropriate message based on whether transactions exist
        if not transactions:
            self.show_message("❌ Unable to clear transactions. None exist.")
        else:
            self.show_message("🗑️ Clearing transactions...")
            # Call the controller to delete all transactions
            TransactionController.clear_all_transactions()
            # Reload the transaction list after a short delay
            self.after(800, lambda: self.load_transactions(reason="cleared"))

    # Helper method to display a temporary message on screen
    def show_message(self, text, duration=1500):
        """Show a temporary label in the center."""
        self.message_label.config(text=text)
        self.message_label.pack(pady=10)

        # Automatically hide the message after the specified duration
        self.after(duration, self.message_label.pack_forget)

    # Method to start the process of loading transactions with appropriate messaging
    def load_transactions(self, reason="default"):
        # Hide any previous message label
        self.message_label.pack_forget()

        # Show appropriate loading message based on the context
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

        # Schedule the actual data load to happen after a short delay for UX
        self.after(800, self.finish_loading)

    # Method that actually fetches the data and populates the table
    def finish_loading(self):
        # Get all transactions from the controller
        transactions = SummaryController.get_all_transactions() or []

        # Convert transactions to the format needed for the table
        rows = [
            (t["name"], t["amount"], t["category"], t["date"], t["type"])
            for t in transactions
        ]

        # Clear the old table data and load the new data
        self.transaction_table.clear()
        self.transaction_table.load_data(rows)

        # Hide the loading label
        self.loading_label.pack_forget()

        # Display the table with the new data
        self.transaction_table.pack(pady=10, fill="x")

    # Callback method called when the dashboard is first shown
    def on_show_first_load(self):
        self.load_transactions(reason="first_load")

    # Callback method called when returning from the Add Income screen
    def on_show_after_income(self):
        self.load_transactions(reason="income_added")

    # Callback method called when returning from the Add Expense screen
    def on_show_after_expense(self):
        self.load_transactions(reason="expense_added")

    # Callback method called when navigating home from other screens
    def on_show_home(self):
        self.load_transactions(reason="default")

