# Import tkinter widget utilities
import tkinter.ttk as ttk

# Custom frame class that centers content nicely
class Center(ttk.Frame):
    # Initialize the centered frame
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Place the frame in the center of its parent
        self.grid(row=0, column=0)

