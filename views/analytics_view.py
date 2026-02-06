import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controllers.summary_controller import SummaryController
from controllers.analytics_controller import AnalyticsController


class AnalyticsView(ttk.Frame):
    """View that displays simple matplotlib charts for transactions."""

    def __init__(self, parent):
        super().__init__(parent, style="App.TFrame")

        self.parent = parent

        # Center container
        self.center = ttk.Frame(self, style="App.TFrame")
        self.center.grid(row=0, column=0, sticky="nsew")

        # Header
        ttk.Label(self.center, text="Analytics", style="Header.TLabel").pack(pady=12)

        # Placeholder for matplotlib canvas or error message
        self.canvas_container = ttk.Frame(self.center, style="App.TFrame")
        self.canvas_container.pack(fill="both", expand=True, padx=10, pady=6)

        # Back button
        ttk.Button(
            self.center,
            text="⬅ Back to Dashboard",
            style="Secondary.TButton",
            command=lambda: parent.show_frame("dashboard", reason="home")
        ).pack(pady=10)

        # Keep a reference to the canvas widget so we can destroy it when redrawing
        self._canvas_widget = None

    def on_show_home(self):
        # When the view is shown, draw the chart
        self.draw_expense_by_category()

    def draw_expense_by_category(self):
        # Fetch expense category data via the analytics controller
        categories = AnalyticsController.get_expense_categories() or []

        # If no data, show a message
        if not categories:
            for child in self.canvas_container.winfo_children():
                child.destroy()

            ttk.Label(
                self.canvas_container,
                text="No expense data available",
                style="Form.TLabel",
            ).pack(pady=20)
            return

        labels = [c["category"] for c in categories]
        values = [c["total"] for c in categories]

        # Remove existing canvas
        for child in self.canvas_container.winfo_children():
            child.destroy()

        fig = Figure(figsize=(6, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(labels, values, color="#7C3AED")
        ax.set_title("Expenses by Category")
        ax.set_ylabel("Amount")
        ax.tick_params(axis='x', rotation=45)

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_container)
        canvas.draw()
        widget = canvas.get_tk_widget()
        widget.pack(fill="both", expand=True)
        self._canvas_widget = widget
        widget.pack(fill="both", expand=True)

        # store reference
        self._canvas_widget = widget
