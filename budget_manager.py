class BudgetManager:
    """Manage a monthly budget and compare it with total spending."""

    def __init__(self, budget=0):
        self.budget = round(float(budget), 2)

    def set_budget(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError("Budget cannot be negative.")
        self.budget = round(amount, 2)

    def remaining_budget(self, total_expenses):
        return round(self.budget - float(total_expenses), 2)

    def budget_status(self, total_expenses):
        remaining = self.remaining_budget(total_expenses)

        if self.budget == 0:
            return "No budget set."
        if remaining < 0:
            return f"Budget exceeded by ₹{abs(remaining):.2f}"
        return f"Budget remaining: ₹{remaining:.2f}"
