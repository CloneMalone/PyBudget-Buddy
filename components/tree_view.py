# Import treeview widget from tkinter
from tkinter import ttk

# Custom TreeView class that extends the standard treeview for displaying data tables
class TreeView(ttk.Treeview):
    # Initialize the treeview with columns and optional custom headings
    def __init__(self, parent, columns, headings=None):
        super().__init__(
            parent,
            columns=columns,
            show="headings",
            style="Custom.Treeview"
        )

        # Store the columns configuration
        self.columns_config = columns

        # Use default column names as headings if custom ones aren't provided
        headings = headings or {col: col.title() for col in columns}

        # Configure each column's heading and appearance
        for col in columns:
            self.heading(col, text=headings.get(col, col))
            self.column(col, anchor="center", stretch=True)

    # Helper method to add multiple rows of data to the table
    def load_data(self, rows):
        """Insert multiple rows into the table"""

        for row in rows:
            self.insert("", "end", values=row)

    # Helper method to remove all rows from the table
    def clear(self):
        """Remove all rows"""
        for item in self.get_children():
            self.delete(item)

