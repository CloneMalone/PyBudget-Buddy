# PyBudgetBuddy — Education Guide

This document explains the project structure, the purpose of each file/group of code, and the runtime flow from the main entrypoint through the UI to the database. Explanations are casual and direct. No abstract metaphors.

Summary / quick map:
- `app.py` — program entrypoint and window setup.
- `views/` — UI screens (Dashboard, Add Income/Expense, lists, analytics).
- `controllers/` — glue that coordinates services with views; formats data for display.
- `services/` — business logic that reads/writes the database.
- `models/` — data structures and DB helpers.
- `components/` & `frames/` — small UI building blocks used by views.
- `styles/` — global styling and theme configuration.
- `memory.md`, `rules.md`, `plan.md` — project management and operating rules.

How to use this guide
- Read from top to bottom for runtime flow.
- Jump to any file section for focused explanations.

---

## Runtime Flow (high level)

1. `app.py` is executed. It creates a Tk root window and constructs `MainView`.
2. `MainView` applies global styles and constructs all view frames, stacking them in the same grid cell.
3. The dashboard frame (`DashboardView`) is shown first. It loads transactions by calling the `SummaryController`.
4. Controllers call services to fetch data from the database (via `models/database.py`).
5. When the user navigates (buttons), `MainView.show_frame()` brings the target frame to the front and optionally calls a lifecycle callback on that frame.
6. Views render UI only and call controllers for data or to run actions (e.g., adding transactions). Controllers delegate DB writes to services.

This separation keeps math and data access out of views (see `rules.md` rule #1 under Custom Rules).

---

## File-by-file explanations

Each file below has a short purpose line, then a grouped explanation of its code.

### `app.py`
- Purpose: application entrypoint and main Tk window initialization.
- Groups:
  - Imports: `tkinter`, `MainView`, `GlobalStyles`, `init_db_background`, `system`.
  - `main()` function: creates a `Tk()` root, sets title, size, and disables resize, constructs `MainView(root)`, calls `init_db_background()` to initialize the database on a separate thread (so UI doesn't block), clears the console via `system('cls')`, and starts `root.mainloop()`.
  - `if __name__ == '__main__'`: runs `main()` when the file is executed directly.

Why it matters: `init_db_background()` prevents the UI freezing while the DB file is created the first time.

### `models/database.py`
- Purpose: database file path, connection helpers, and schema initialization.
- Groups:
  - Config: `DB_PATH = "data/finance.db"` — relative path for the sqlite file.
  - `get_connection()`: returns `sqlite3.connect(DB_PATH)` (no row factory set; services use tuple-based access or convert to dicts where needed).
  - `init_db()`: ensures the `data` folder exists, opens a connection, and executes the `CREATE TABLE IF NOT EXISTS transactions (...)` SQL. The `date` column stores text; `type` is constrained to `('Income','Expense')`.
  - `init_db_background()`: checks if DB exists; if not, starts a daemon thread calling `init_db()`.

Notes: Keeping DB path relative is convenient for single-user desktop apps. The table schema stores amounts as REAL.

### `models/transaction.py`
- Purpose: simple `Transaction` class used to construct data objects before insertion.
- Groups:
  - Imports: `date` from `datetime`.
  - `Transaction.__init__`: stores `name`, `amount`, `category`, sets `_date` to `date.today()`, and `_type` for `'Income'` or `'Expense'`.
  - `date` property: returns formatted date string `MM/DD/YYYY` for display.

Note: Views and controllers pass `Transaction` instances to the `TransactionService` for insertion.

### `services/transaction_service.py`
- Purpose: persistence for writing transactions and clearing all transactions.
- Groups:
  - Imports: `get_connection` and the `Transaction` model.
  - `add(transaction)`: prepares a parametrized SQL `INSERT` statement, extracts values from the `Transaction` instance (using the stored `_date` and `_type`), executes, commits, and closes. Also prints the executed SQL and values for debugging.
  - `clear_all()`: executes `DELETE FROM transactions`, commits, and closes.

Important: This module performs writes and commits; controllers call these methods to persist data.

### `services/summary_service.py`
- Purpose: read-only queries and summary math for totals and listings.
- Groups:
  - `get_all_transactions()`: runs `SELECT * FROM transactions ORDER BY date DESC, id DESC`, fetches rows, prints debug info, then constructs a list of dictionaries with keys `id,name,amount,category,date,type` by mapping tuple positions to keys. Returns list of dicts.
  - `get_total_income_and_expenses()`: selects `amount, type` for all transactions, iterates rows, and sums amounts into `total_income` and `total_expenses` depending on `type.lower()`.

Why controllers call this: Services return raw data (or totals). Controllers format data for views (currency formatting, filtering) — fits the architecture in `rules.md`.

### `controllers/summary_controller.py`
- Purpose: transform `SummaryService` data into UI-friendly shapes.
- Groups:
  - `get_all_transactions()`: calls `SummaryService.get_all_transactions()`. If no rows, returns `[]`. Otherwise converts each service row (a dict) into a formatted dict where `amount` becomes a currency string (e.g., `"$ 12.00"`) and other fields are passed through.
  - `get_total_income_and_expenses()`: calls the service totals and formats them as currency strings.
  - `get_expenses_summary()` and `get_income_summary()`: both call `SummaryService.get_all_transactions()` and iterate to select rows where `type` matches `expense` or `income` respectively. They aggregate totals as numbers and also build `category_totals` mapping category → numeric total. They convert the mapping into a sorted `categories` list of objects `{'category': name, 'total': value}` sorted descending. The method returns a dict with `total` (formatted string), `rows` (list of original txn dicts), and `categories` (the aggregated list used by the views).

Design note: Controllers do light presentation formatting (currency) and aggregation; heavier DB work remains in services.

### `controllers/transaction_controller.py`
- Purpose: simple wrappers to call the transaction service.
- Groups:
  - `add_transaction(transaction)`: calls `TransactionService.add(transaction)`.
  - `clear_all_transactions()`: calls `TransactionService.clear_all()`.

This keeps views thin — they call controller methods rather than services directly.

### `components/tree_view.py`
- Purpose: small convenience wrapper around `ttk.Treeview` for table display.
- Groups:
  - Class `TreeView(ttk.Treeview)`: constructor sets `show='headings'` and a custom style `Custom.Treeview`, stores `columns_config`, and sets headings (optionally with emoji labels provided by callers), and configures each column's anchor and stretch.
  - `load_data(rows)`: inserts rows via `self.insert("","end",values=row)`.
  - `clear()`: deletes all child items.

Why: keeps repeated Treeview setup in one place and simplifies view code.

### `frames/center.py` and `frames/button_group.py`
- `Center`: a small frame subclass that applies `App.TFrame` style and places itself with `grid(row=0,column=0)`. Views use `Center(self)` to get a centered container.
- `ButtonGroup`: a small frame that packs itself with `pady=10` so buttons align consistently. The Dashboard constructs a `ButtonGroup` and packs many buttons side-by-side inside it.

These helpers are purely presentational and keep view layout consistent.

### `styles/global_styles.py`
- Purpose: central place to define colors, fonts and apply ttk styles.
- Groups:
  - Color and font constants near the top (background, button colors, treeview colors, font tuples like `("Century Gothic", 10)`).
  - `apply_styles(style)`: uses the `clam` theme and calls `style.configure()` and `style.map()` to define many named styles: `App.TFrame`, `Primary.TButton`, `Secondary.TButton`, `Danger.TButton`, `Info.TButton`, `Header.TLabel`, `SubHeader.TLabel`, `Form.TLabel`, `Form.TEntry`, `Custom.Treeview`, `Custom.Treeview.Heading`, `Loading.TLabel`, and also `CategoryCard.TFrame`, `CategoryName.TLabel`, `CategoryAmount.TLabel` for the category summary cards. The category styles include the padding and larger fonts we added.

Why: centralizing these keeps the look consistent and lets all views reuse named styles rather than repeating low-level widget options.

### `views/main_view.py`
- Purpose: single frame that constructs all pages and performs navigation between them.
- Groups:
  - Style application: constructs `ttk.Style()` and calls `GlobalStyles.apply_styles(self.style)`.
  - Frame creation: builds `DashboardView`, `AddIncomeView`, `AddExpenseView`, `ExpenseListView`, `IncomeListView`, and `AnalyticsView` and stores them in `self.frames` keyed by name.
  - Grid stacking: places every frame at `row=0,column=0,sticky='nsew'` so they overlap; `tkraise()` shows the active frame.
  - `show_frame(name, reason=None)`: raises the frame and optionally calls lifecycle callbacks `on_show_first_load`, `on_show_after_income`, `on_show_after_expense`, or `on_show_home` depending on the `reason` parameter. Views implement these callbacks as needed.

This file is the router of the UI and the central place to manage screen transitions.

### `views/dashboard_view.py`
- Purpose: the main dashboard where users land. Shows header, buttons, and a transactions table.
- Groups:
  - Constructor: creates `Center(self)`, header label, `ButtonGroup` and all the action buttons: Add Income, Add Expense, View Expenses, View Income, Analytics, Clear All Transactions. Buttons call `parent.show_frame()` or bound methods.
  - `clear_all_transactions()`: uses `SummaryController.get_all_transactions()` to detect if anything exists, shows messages via `show_message()` and calls `TransactionController.clear_all_transactions()` followed by `self.after()` to refresh the list.
  - `show_message(text,duration)`: packs `self.message_label` and hides it after `duration` ms.
  - `load_transactions(reason)`: shows a `loading_label` depending on `reason` and schedules `finish_loading()` via `after(800,...)` to give a short UX delay.
  - `finish_loading()`: gets transactions via `SummaryController.get_all_transactions()`, converts them into table rows, clears and loads table via `TreeView`, hides the loading label, and packs the `transaction_table`.
  - Lifecycle callbacks: `on_show_first_load`, `on_show_after_income`, `on_show_after_expense`, `on_show_home` call `load_transactions()` with appropriate reasons.

Important: Dashboard is read-only for the table; adding transactions is done via separate views.

### `views/add_income_view.py` and `views/add_expense_view.py`
- Purpose: simple forms for creating a `Transaction` (Income or Expense).
- Groups (shared pattern):
  - Constructor: creates `Center(self)`, header label, `tk.StringVar()`s for inputs, labeled `ttk.Entry` fields styled with `Form.TEntry`, and a `ButtonGroup` with action buttons.
  - Save button: calls a method (`add_income`/`add_expense`) that validates fields, constructs a `Transaction` instance with `_type` set appropriately, calls `TransactionController.add_transaction(transaction)`, shows a success message on the dashboard by calling `parent.show_frame('dashboard', reason='income_added'/'expense_added')`.

Notes: The controller handles insertion; the view is responsible for collecting user input.

### `views/expense_list_view.py` and `views/income_list_view.py`
- Purpose: views that show only expenses or only income, each with totals and the transaction table.
- Groups:
  - Constructor: `Center(self)`, header label, `total_label`, `categories_frame` (container for the category summary cards), `TreeView` table, and Back button.
  - `on_show_home()`: loads the appropriate data.
  - `load_expenses()` / `load_income()`: clears table, calls `SummaryController.get_expenses_summary()` / `get_income_summary()`, updates `total_label`, calls `render_categories()` with the `categories` list, transforms transactions into table rows and calls `self.table.load_data(rows)`.
  - `render_categories(categories)`: clears the `categories_frame` and, for each category, creates a small `ttk.Frame` styled `CategoryCard.TFrame` with `CategoryName.TLabel` and `CategoryAmount.TLabel` showing the category and total. Cards are packed side-by-side with small spacing.

Design: This keeps category summaries visually accessible above the table.

### `views/analytics_view.py` (new)
- Purpose: simple matplotlib-powered view that draws a bar chart of expenses by category.
- Groups:
  - Constructor: header, a `canvas_container` frame to hold the matplotlib canvas, and a Back button.
  - `on_show_home()`: calls `draw_expense_by_category()`.
  - `draw_expense_by_category()`: lazy-imports `matplotlib` (so the app can run without it installed until this view is used). If import fails, shows a message instructing how to install. Otherwise, it calls `SummaryController.get_expenses_summary()` to fetch aggregated category data, builds a `Figure` and draws a bar chart, packs it via `FigureCanvasTkAgg` inside `canvas_container`.

Why lazy import: Avoids a hard dependency during app startup and provides a user-friendly message in the view if `matplotlib` is missing.

### `rules.md`, `plan.md`, `memory.md`, `README.md`
- Purpose: project guide, plan, log, and README respectively. `rules.md` contains the working rules (controllers/services do math, log changes to memory.md, etc.). `memory.md` is used to record changes made by the AI or devs; when the tool makes edits it appends a short entry.

---

## Architectural summary and reasoning

- Pattern: lightweight MVC
  - Models: `models/` and `services/` (data access and persistence)
  - Views: `views/` (UI screens)
  - Controllers: `controllers/` (presentation logic and orchestration)

- Why this split: keeps UI code simple, testable, and reduces duplication. Business rules and DB access are centralized in services and controllers.

## Typical user flow (detailed)

1. Launch `app.py` → `MainView` constructed → `DashboardView` shown.
2. Dashboard calls `SummaryController.get_all_transactions()` through `load_transactions()` → `SummaryService.get_all_transactions()` queries DB and returns rows → `SummaryController` formats them for UI → dashboard `TreeView` displays them.
3. To add an income: Dashboard's "Add Income" button raises `AddIncomeView`. The form creates a `Transaction` and calls `TransactionController.add_transaction()` → `TransactionService.add()` performs insert and commit. The view then navigates back to the dashboard with reason `income_added`, causing the dashboard to reload.
4. To inspect categories: open `Expenses` or `Income` lists. These call `SummaryController.get_expenses_summary()` / `get_income_summary()` which aggregate categories and return both rows and `categories`. Views render category cards and the table.
5. To see a chart: open `Analytics` from Dashboard. The analytics view lazy-imports `matplotlib`, pulls category aggregates from the controller, and draws a bar chart embedded inside Tk.

---

## Tips for extending the project
- Add validation in views for amounts (ensure numeric input) before creating `Transaction`.
- Add `row_factory` in `get_connection()` to return `sqlite3.Row` for easier dictionary-like access inside services.
- Add unit tests for `SummaryService` aggregations and `TransactionService` writes using a temporary sqlite DB file.
- Add pagination or a limit for category cards in `render_categories()` if many categories exist.

---

If you want, I can also produce a line-by-line export that annotates every single file line exactly (very verbose). This file groups lines logically for easier reading; tell me if you prefer the fully literal line-by-line commentary.
