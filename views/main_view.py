import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

from views.dashboard_view import DashboardView
from views.add_expense_view import AddExpenseView
from views.add_income_view import AddIncomeView
from views.transaction_list_view import TransactionListView
from views.expense_list_view import ExpenseListView
from views.income_list_view import IncomeListView

class MainView(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, style="App.TFrame")

        # Apply global styles
        self.style = ttk.Style()
        GlobalStyles.apply_styles(self.style)
        
        # Fill the entire window within root
        self.pack(fill="both", expand=True)

        # Dictionary to store all views
        self.frames = {}

        self.frames["dashboard"] = DashboardView(self)
        self.frames["add_income"] = AddIncomeView(self)
        self.frames["add_expense"] = AddExpenseView(self)
        self.frames["transactions"] = TransactionListView(self)
        self.frames["expenses"] = ExpenseListView(self)
        self.frames["income"] = IncomeListView(self)

        # Allow the rows and columns to stretch and
        # fill white space
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)


        # Start with dashboard
        self.show_frame("dashboard", reason="first_load")


    def show_frame(self, name, reason=None):
        frame = self.frames[name]
        frame.tkraise()

        # Call the appropriate on_show method if it exists
        if hasattr(frame, "on_show_first_load") and reason == "first_load":
            frame.on_show_first_load()
        elif hasattr(frame, "on_show_after_income") and reason == "income_added":
            frame.on_show_after_income()
        elif hasattr(frame, "on_show_after_expense") and reason == "expense_added":
            frame.on_show_after_expense()
        elif hasattr(frame, "on_show_home") and reason == "home":
            frame.on_show_home()
