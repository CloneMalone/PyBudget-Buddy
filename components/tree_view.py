from tkinter import ttk

class TreeView(ttk.Treeview):
    def __init__(self, parent, columns, headings=None):
        super().__init__(
            parent,
            columns=columns,
            show="headings",
            style="Custom.Treeview"
        )

        self.columns_config = columns

        # Headings: default to column names if not provided
        headings = headings or {col: col.title() for col in columns}

        for col in columns:
            self.heading(col, text=headings.get(col, col))
            self.column(col, anchor="center", stretch=True)

    # Reusable API for loading data
    def load_data(self, rows):
        """Insert multiple rows into the table"""

        for row in rows:
            self.insert("", "end", values=row)

    def clear(self):
        """Remove all rows"""
        for item in self.get_children():
            self.delete(item)
