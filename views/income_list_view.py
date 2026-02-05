# Import tkinter libraries for building the UI
import tkinter.ttk as ttk

# Import custom frame components
from frames.center import Center
from components.tree_view import TreeView

# Import controller
from controllers.summary_controller import SummaryController


# View screen for displaying income transactions only
class IncomeListView(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        self.parent = parent

        # Centered layout container
        self.center = Center(self)

        # Screen header
        ttk.Label(
            self.center,
            text="Income",
            style="Header.TLabel"
        ).pack(pady=20)

        # Total income label
        self.total_label = ttk.Label(
            self.center,
            text="Total: $0.00",
            style="SubHeader.TLabel"
        )
        self.total_label.pack(pady=10)

        # Container for category summary cards
        self.categories_frame = ttk.Frame(self.center, style="App.TFrame")
        self.categories_frame.pack(pady=6, fill="x")
        # Income table
        self.table = TreeView(
            self.center,
            columns=("name", "amount", "category", "date"),
            headings={
                "name": "📝 Name",
                "amount": "💰 Amount",
                "category": "📗 Category",
                "date": "📅 Date",
            }
        )
        self.table.pack(pady=10, fill="x")

        # Back button
        ttk.Button(
            self.center,
            text="⬅ Back to Dashboard",
            style="Secondary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home")
        ).pack(pady=20)

    # Called when navigating to this screen
    def on_show_home(self):
        self.load_income()

    # Load income data from the controller
    def load_income(self):
        # Clear existing rows
        self.table.clear()

        # Fetch pre-processed income data
        summary = SummaryController.get_income_summary()

        # Update total label
        self.total_label.config(text=f"Total: {summary['total']}")

        # Render category summary cards
        self.render_categories(summary.get("categories", []))

        # Convert rows for table display
        rows = []

        for txn in summary["rows"]:
            rows.append(
                (
                    txn["name"],
                    f"$ {txn['amount']:.2f}",
                    txn["category"],
                    txn["date"],
                )
            )

        self.table.load_data(rows)

    # Render compact category summary cards
    def render_categories(self, categories):
        # Clear existing category widgets
        for child in self.categories_frame.winfo_children():
            child.destroy()

        # Create a small card for each category
        for cat in categories:
            card = ttk.Frame(self.categories_frame, style="CategoryCard.TFrame")
            name = ttk.Label(card, text=cat["category"], style="CategoryName.TLabel")
            amount = ttk.Label(card, text=f"$ {cat['total']:.2f}", style="CategoryAmount.TLabel")
            name.pack(anchor="w")
            amount.pack(anchor="w")
            card.pack(side="left", padx=8, pady=4)
