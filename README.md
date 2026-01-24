# PyBudgetBuddy 💰

Your friendly personal finance buddy! PyBudgetBuddy is a simple, elegant desktop application that helps you track your income and expenses all in one place. Built with Python and Tkinter, it's lightweight, fast, and easy to use.

## What's This About?

PyBudgetBuddy lets you:
- **Track Income** - Log all your money coming in (salary, side gigs, gifts, etc.)
- **Track Expenses** - Keep tabs on where your money's going (groceries, subscriptions, gas, etc.)
- **View Summaries** - See your income vs. expenses at a glance with detailed analytics
- **Browse History** - Check out all your transactions whenever you need to
- **Organize by Category** - Categorize your transactions to understand spending patterns

Think of it as your personal financial journal, but actually useful and not boring.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- tkinter (usually comes with Python)

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd PyBudgetBuddy
   ```
3. Run the app:
   ```bash
   python app.py
   ```

That's it! The app window should pop up, and you're ready to start tracking.

## How to Use

### Dashboard
When you first open PyBudgetBuddy, you'll land on the dashboard. This is your home base where you can:
- Add a new income entry
- Add a new expense entry
- Clear all transactions (be careful with this one!)
- See your financial overview

### Adding Income
Click "Add Income" from the dashboard and fill in:
- **Name** - What's this income from? (e.g., "Paycheck", "Freelance work")
- **Amount** - How much did you make?
- **Source** - Where did it come from? (e.g., "My Day Job", "Side Project")

Hit save and it's recorded!

### Adding Expenses
Click "Add Expense" and fill in:
- **Name** - What did you buy? (e.g., "Coffee", "Gas")
- **Amount** - How much did it cost?
- **Category** - What type of expense? (e.g., "Food", "Transportation", "Entertainment")

Done! It's automatically dated and stored.

### Viewing Your Data
- **All Transactions** - See every transaction you've entered
- **Income List** - Just your income entries
- **Expense List** - Just your expenses
- **Summary** - Get the breakdown of where your money's going and where it's coming from

Each transaction is automatically dated with today's date, so you can track everything over time.

## Project Architecture

This project follows the **MVC (Model-View-Controller) Pattern** to keep things clean and organized.

### Directory Structure

```
PyBudgetBuddy/
├── models/              # The data layer
│   ├── transaction.py   # Transaction data object
│   └── database.py      # Database setup and connections
├── views/               # The UI layer (what you see)
│   ├── main_view.py     # Main window and frame manager
│   ├── dashboard_view.py
│   ├── add_income_view.py
│   ├── add_expense_view.py
│   ├── transaction_list_view.py
│   ├── income_list_view.py
│   └── expense_list_view.py
├── controllers/         # The logic layer (makes decisions)
│   ├── transaction_controller.py
│   └── summary_controller.py
├── services/            # Business logic and data operations
│   ├── transaction_service.py
│   ├── summary_service.py
│   └── analytics_service.py
├── frames/              # Reusable UI components
│   ├── center.py        # Centered container
│   └── button_group.py  # Grouped button container
├── components/          # Custom widgets
│   └── tree_view.py     # Table-like display component
├── styles/              # Visual styling
│   └── global_styles.py
├── data/                # Where your data lives
│   └── finance.db       # SQLite database (auto-created)
└── app.py              # Main entry point
```

### Design Patterns Used

**Model-View-Controller (MVC)**
- **Models** handle data (transactions, database schema)
- **Views** handle the user interface (what gets displayed)
- **Controllers** act as the middleman, handling user actions and updating models

**Service Layer**
- Services contain business logic separate from controllers
- Makes code reusable and testable
- Examples: TransactionService, SummaryService, AnalyticsService

**Reusable Components**
- Custom frames (Center, ButtonGroup) keep the UI DRY (Don't Repeat Yourself)
- Components like TreeView are built once and reused across views

**Separation of Concerns**
- Database logic is separate (models/database.py)
- Styling is centralized (styles/global_styles.py)
- Each view handles only its own screen
- Each controller handles only its domain (transactions, summaries)

## Data Storage

PyBudgetBuddy uses **SQLite** (a lightweight, file-based database) to store your data. All your transactions are saved in `data/finance.db` automatically whenever you add an entry.

### Transaction Schema
Each transaction has:
- **ID** - Unique identifier
- **Name** - What it's for
- **Amount** - How much (in dollars)
- **Category** - Income source or expense type
- **Date** - When it happened (auto-set to today)
- **Type** - Either "Income" or "Expense"

## Technical Stack

| Part | Technology |
|------|-----------|
| **Language** | Python 3.7+ |
| **UI Framework** | Tkinter |
| **Database** | SQLite |
| **Architecture** | MVC + Service Layer |

## Tips & Tricks

- **Dates are automatic** - Every transaction is automatically dated with today's date
- **Edit categories as needed** - You can use any category names you want for expenses
- **Clear all with caution** - Once you clear all transactions, they're gone (no undo)
- **Keep it organized** - Use consistent category names to make analytics easier

## Troubleshooting

**App won't start?**
- Make sure Python 3.7+ is installed
- Check that tkinter is available: `python -m tkinter` should open a test window

**Database errors?**
- The `data/` folder will be created automatically
- If `finance.db` gets corrupted, just delete it and start fresh (you'll lose your history though!)

**UI looks weird?**
- This is a desktop app, so appearance might vary by OS

## Future Ideas

Want to make it better? Here are some ideas:
- Export data to CSV or PDF
- Budget alerts ("You're overspending on eating out!")
- Recurring transactions (automatic monthly bills)
- Charts and graphs for better visualization
- Data import from bank statements
- Search and filter transactions
- Multiple accounts/budgets

## License

This is a school project - feel free to use it, learn from it, and build on it!

---

Happy budgeting! 🎯
