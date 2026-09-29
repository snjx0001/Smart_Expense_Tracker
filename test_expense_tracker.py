import tempfile
import unittest
from pathlib import Path

from budget_manager import BudgetManager
from expense_manager import ExpenseManager
from reports import ReportGenerator
from storage import Storage
from validation import (
    validate_amount,
    validate_category,
    validate_date,
    validate_description,
)


class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.manager = ExpenseManager()
        self.manager.add_expense(250, "Food", "Lunch", "2026-09-26")
        self.manager.add_expense(500, "Transport", "Taxi", "2026-09-26")

    def test_total(self):
        self.assertEqual(self.manager.total_expenses(), 750)

    def test_search(self):
        self.assertEqual(len(self.manager.search("food")), 1)
        self.assertEqual(len(self.manager.search("taxi")), 1)

    def test_update(self):
        updated = self.manager.update_expense(
            0, 300, "Food", "Dinner", "2026-09-27"
        )
        self.assertEqual(updated["amount"], 300)
        self.assertEqual(updated["description"], "Dinner")

    def test_delete(self):
        self.manager.delete_expense(0)
        self.assertEqual(len(self.manager.get_expenses()), 1)

    def test_filter_by_date(self):
        self.assertEqual(len(self.manager.filter_by_date("2026-09-26")), 2)

    def test_validation(self):
        self.assertEqual(validate_amount("100.50"), 100.50)
        self.assertEqual(validate_category("food"), "Food")
        self.assertEqual(validate_date("2026-09-26"), "2026-09-26")
        self.assertEqual(validate_description("Lunch"), "Lunch")

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("-10")

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            validate_category("Unknown")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            validate_date("26-09-2026")

    def test_budget(self):
        budget = BudgetManager(1000)
        self.assertEqual(budget.remaining_budget(750), 250)
        self.assertEqual(budget.budget_status(750), "Budget remaining: ₹250.00")

    def test_report(self):
        report = ReportGenerator()
        summary = report.summary(self.manager.get_expenses())
        self.assertEqual(summary["total"], 750)
        self.assertEqual(summary["count"], 2)

    def test_storage(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "expenses.csv"
            storage = Storage(path)
            storage.save(self.manager.get_expenses())
            loaded = storage.load()
            self.assertEqual(len(loaded), 2)
            self.assertEqual(loaded[0]["category"], "Food")


if __name__ == "__main__":
    unittest.main()
