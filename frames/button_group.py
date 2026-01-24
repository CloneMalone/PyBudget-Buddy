import tkinter.ttk as ttk

class ButtonGroup(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        self.pack(pady=10)