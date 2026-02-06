# Analytics service: prepares aggregated data for analytics-related views/controllers
from services.summary_service import SummaryService  # Import service that provides raw transaction data


class AnalyticsService:
    @staticmethod
    def get_expense_categories():
        # Retrieve all transactions from the summary service
        transactions = SummaryService.get_all_transactions()

        # Dictionary to accumulate total expense amounts per category
        # Example shape: { "Food": 120.50, "Rent": 950.00 }
        totals_by_category = {}

        # Iterate through every transaction record
        for transaction in transactions:
            # Skip any transaction that is not an Expense
            if transaction.get("type") != "Expense":
                continue

            # Safely attempt to parse the transaction amount as a float
            # If the value is missing, null, or invalid, default to 0.0
            try:
                amount = float(transaction.get("amount") or 0)
            except (TypeError, ValueError):
                amount = 0.0

            # Retrieve the transaction category
            # Default to "Uncategorized" if the category is missing or empty
            category = transaction.get("category") or "Uncategorized"

            # Add the amount to the running total for this category
            # If the category does not yet exist, start its total at 0.0
            totals_by_category[category] = (
                totals_by_category.get(category, 0.0) + amount
            )

        # Convert the category totals dictionary into a sorted list of tuples
        # Sort by total amount (descending) so highest expenses appear first
        sorted_categories = sorted(
            totals_by_category.items(),          # (category, total) pairs
            key=lambda item: item[1],             # Sort by the total value
            reverse=True,                         # Highest totals first
        )

        # Transform the sorted data into a list of dictionaries
        # This format is convenient for JSON responses or templates
        return [
            {"category": category, "total": total}
            for category, total in sorted_categories
        ]
