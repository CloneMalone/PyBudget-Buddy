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
