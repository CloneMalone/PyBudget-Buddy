import tkinter.ttk as ttk

class Center(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        self.grid(row=0, column=0)
