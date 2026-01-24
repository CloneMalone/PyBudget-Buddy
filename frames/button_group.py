# Import tkinter widget utilities
import tkinter.ttk as ttk

# Custom frame class for grouping buttons horizontally
class ButtonGroup(ttk.Frame):
    # Initialize the button group frame
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        # Pack the frame with padding for better spacing
        self.pack(pady=10)