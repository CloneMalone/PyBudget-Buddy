import tkinter as tk
from views.main_view import MainView
from styles.global_styles import GlobalStyles

def main():
    root = tk.Tk()
    root.title("PyBudget Buddy")
    root.geometry("1200x600")
    root.resizable(False, False)
   

    # Main frame manager
    main_view = MainView(root)

    root.mainloop()

if __name__ == "__main__":
    main()
