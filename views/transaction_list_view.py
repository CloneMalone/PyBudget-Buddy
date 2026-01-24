import tkinter as tk
import tkinter.ttk as ttk
from styles.global_styles import GlobalStyles

from frames.center import Center

class TransactionListView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # We must place a frame within the current
        # view so that widgets can center properly
        center = Center(self)
        
        ttk.Label(center, text="All Transactions", style="Header.TLabel").pack(pady=20)