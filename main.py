from expense_manager import ExpenseManager
from validation import (
    validate_amount,
    validate_category,
    validate_date,
    validate_description,
)
from storage import Storage
from budget_manager import BudgetManager
from reports import ReportGenerator
from dashboard import Dashboard


def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\nNo.  Date        Category         Amount       Description")
    print("-" * 70)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<4} "
            f"{expense['date']:<11} "
            f"{expense['category']:<16} "
            f"₹{expense['amount']:<10.2f} "
            f"{expense['description']}"
        )


def read_expense_details(prefix=""):
    amount = validate_amount(input(f"{prefix}Amount: "))
    category = validate_category(input(f"{prefix}Category: "))
    description = validate_description(input(f"{prefix}Description: "))
    date = validate_date(input(f"{prefix}Date (YYYY-MM-DD): "))
    return amount, category, description, date


def add_expense(manager, storage):
    try:
        details = read_expense_details()
        manager.add_expense(*details)
        storage.save(manager.get_expenses())
        print("Expense added and saved successfully.")
    except ValueError as error:
        print(f"Error: {error}")


def update_expense(manager, storage):
    print_expenses(manager.get_expenses())
    if not manager.get_expenses():
        return

    try:
        index = int(input("Enter expense number to update: ")) - 1
        details = read_expense_details("New ")
        manager.update_expense(index, *details)
        storage.save(manager.get_expenses())
        print("Expense updated and saved successfully.")
    except (ValueError, IndexError) as error:
        print(f"Error: {error}")


def delete_expense(manager, storage):
    print_expenses(manager.get_expenses())
    if not manager.get_expenses():
        return

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        manager.delete_expense(index)
        storage.save(manager.get_expenses())
        print("Expense deleted and saved successfully.")
    except (ValueError, IndexError) as error:
        print(f"Error: {error}")


def show_summary(manager, reports):
    summary = reports.summary(manager.get_expenses())

    print("\n========== EXPENSE SUMMARY ==========")
    print(f"Total Expenses     : ₹{summary['total']:.2f}")
    print(f"Number of Expenses : {summary['count']}")

    if summary["highest"]:
        highest = summary["highest"]
        print(
            "Highest Expense     : "
            f"₹{highest['amount']:.2f} - "
            f"{highest['category']} ({highest['description']})"
        )

    print("\nCategory totals:")
    if summary["category_totals"]:
        for category, amount in summary["category_totals"].items():
            print(f"  {category:<15} ₹{amount:.2f}")
    else:
        print("  No expenses recorded.")


def show_budget(manager, budget):
    total = manager.total_expenses()
    remaining = budget.remaining_budget(total)

    print("\n========== BUDGET STATUS ==========")
    print(f"Budget          : ₹{budget.budget:.2f}")
    print(f"Total Expenses  : ₹{total:.2f}")
    print(f"Remaining       : ₹{remaining:.2f}")

    if budget.budget == 0:
        print("No budget set.")
    elif remaining < 0:
        print("Budget exceeded!")
    else:
        print("You are within your budget.")


def main():
    manager = ExpenseManager()
    storage = Storage()
    budget = BudgetManager()
    reports = ReportGenerator()
    dashboard = Dashboard()

    manager.expenses = storage.load()

    while True:
        print(
            """
======================================
       SMART EXPENSE TRACKER
======================================
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Search Expense
6. Expense Summary
7. Set Budget
8. Budget Status
9. Save Expenses
10. Exit
======================================
"""
        )

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager, storage)

        elif choice == "2":
            print_expenses(manager.get_expenses())

        elif choice == "3":
            update_expense(manager, storage)

        elif choice == "4":
            delete_expense(manager, storage)

        elif choice == "5":
            keyword = input("Enter category or description to search: ")
            print_expenses(manager.search(keyword))

        elif choice == "6":
            dashboard.display(manager.get_expenses(), budget, reports)

        elif choice == "7":
            try:
                amount = validate_amount(input("Enter monthly budget: "))
                budget.set_budget(amount)
                print(f"Monthly budget set to ₹{amount:.2f}")
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "8":
            show_budget(manager, budget)

        elif choice == "9":
            storage.save(manager.get_expenses())
            print("All expenses saved successfully.")

        elif choice == "10":
            storage.save(manager.get_expenses())
            print("Data saved. Thank you for using Smart Expense Tracker!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 10.")


if __name__ == "__main__":
    main()
