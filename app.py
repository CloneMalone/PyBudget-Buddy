# Import necessary libraries
import tkinter as tk
from views.main_view import MainView
from styles.global_styles import GlobalStyles
from models.database import init_db_background

# Main entry point for the application
def main():
    # Create the root window and set up basic properties
    root = tk.Tk()
    root.title("PyBudget Buddy")
    root.geometry("1200x600")
    root.resizable(False, False)

    # Set up the main view which handles all the screens/pages
    main_view = MainView(root)

    # Initialize the database on a separate thread so it doesn't freeze the UI
    init_db_background()

    # Start the app and listen for user interactions
    root.mainloop()

# Only run main if this is the direct entry point
if __name__ == "__main__":
    main()
