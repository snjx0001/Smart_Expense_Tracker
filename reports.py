from collections import defaultdict


class ReportGenerator:
    """Generate summaries and reports from expense records."""

    def category_totals(self, expenses):
        totals = defaultdict(float)

        for expense in expenses:
            totals[expense["category"]] += expense["amount"]

        return {category: round(amount, 2) for category, amount in sorted(totals.items())}

    def monthly_total(self, expenses, year_month):
        total = sum(
            expense["amount"]
            for expense in expenses
            if expense["date"].startswith(year_month)
        )
        return round(total, 2)

    def highest_expense(self, expenses):
        return max(expenses, key=lambda expense: expense["amount"], default=None)

    def summary(self, expenses):
        return {
            "count": len(expenses),
            "total": round(sum(expense["amount"] for expense in expenses), 2),
            "highest": self.highest_expense(expenses),
            "category_totals": self.category_totals(expenses),
        }
