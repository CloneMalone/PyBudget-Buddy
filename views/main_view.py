# Import tkinter libraries for building the UI
import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

# Import all the different view/page screens
from views.dashboard_view import DashboardView
from views.add_expense_view import AddExpenseView
from views.add_income_view import AddIncomeView
from views.expense_list_view import ExpenseListView
from views.income_list_view import IncomeListView

# Main application frame that manages all the different screens/pages
class MainView(ttk.Frame):
    # Initialize the main view with all screens
    def __init__(self, root):
        super().__init__(root, style="App.TFrame")

        # Apply the global style theme to the entire application
        self.style = ttk.Style()
        GlobalStyles.apply_styles(self.style)
        
        # Make this frame fill the entire window
        self.pack(fill="both", expand=True)

        # Create a dictionary to store all the different screens/pages
        self.frames = {}

        # Create each view screen and add it to the dictionary
        self.frames["dashboard"] = DashboardView(self)
        self.frames["add_income"] = AddIncomeView(self)
        self.frames["add_expense"] = AddExpenseView(self)
        self.frames["expenses"] = ExpenseListView(self)
        self.frames["income"] = IncomeListView(self)

        # Configure grid layout to stretch and fill white space
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Stack all frames on top of each other in the same grid location
        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(0, weight=1)


        # Start by showing the dashboard screen
        self.show_frame("dashboard", reason="first_load")


    # Method to switch between different screens
    def show_frame(self, name, reason=None):
        # Bring the selected frame to the front
        frame = self.frames[name]
        frame.tkraise()

        # Call the appropriate callback method on the frame if it exists, based on the reason
        if hasattr(frame, "on_show_first_load") and reason == "first_load":
            frame.on_show_first_load()
        elif hasattr(frame, "on_show_after_income") and reason == "income_added":
            frame.on_show_after_income()
        elif hasattr(frame, "on_show_after_expense") and reason == "expense_added":
            frame.on_show_after_expense()
        elif hasattr(frame, "on_show_home") and reason == "home":
            frame.on_show_home()

