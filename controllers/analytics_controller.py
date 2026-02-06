from services.analytics_service import AnalyticsService


class AnalyticsController:
    @staticmethod
    def get_expense_categories():
        # Return expense categories prepared for views.
        return AnalyticsService.get_expense_categories()
