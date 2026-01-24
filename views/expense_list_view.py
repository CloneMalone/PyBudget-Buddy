# Import tkinter libraries for building the UI
import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

# Import custom frame components
from frames.center import Center

# View screen for displaying expense transactions only
class ExpenseListView(ttk.Frame):
    # Initialize the Expense List screen
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Create a centered frame for better layout
        # (We must place a frame within the current view so that widgets can center properly)
        center = Center(self)

        # Add the "Expenses" header label
        ttk.Label(center, text="Expenses", style="Header.TLabel").pack(pady=20)