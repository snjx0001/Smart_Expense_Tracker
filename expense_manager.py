class ExpenseManager:
    """Store and manage expense records in memory."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description, date):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        expense = {
            "amount": round(float(amount), 2),
            "category": category.strip(),
            "description": description.strip(),
            "date": date,
        }
        self.expenses.append(expense)
        return expense

    def update_expense(self, index, amount, category, description, date):
        if not 0 <= index < len(self.expenses):
            raise IndexError("Invalid expense number.")
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        self.expenses[index] = {
            "amount": round(float(amount), 2),
            "category": category.strip(),
            "description": description.strip(),
            "date": date,
        }
        return self.expenses[index]

    def delete_expense(self, index):
        if not 0 <= index < len(self.expenses):
            raise IndexError("Invalid expense number.")
        return self.expenses.pop(index)

    def get_expenses(self):
        return list(self.expenses)

    def search(self, keyword):
        keyword = keyword.strip().lower()
        return [
            expense
            for expense in self.expenses
            if keyword in expense["category"].lower()
            or keyword in expense["description"].lower()
        ]

    def search_by_category(self, category):
        category = category.strip().lower()
        return [
            expense
            for expense in self.expenses
            if expense["category"].lower() == category
        ]

    def filter_by_date(self, date):
        return [expense for expense in self.expenses if expense["date"] == date]

    def total_expenses(self):
        return round(sum(expense["amount"] for expense in self.expenses), 2)
