class Dashboard:
    """Display a summary of expenses and budget status."""

    def display(self, expenses, budget_manager, report_generator):
        summary = report_generator.summary(expenses)

        print("\n========== EXPENSE SUMMARY ==========")
        print(f"Number of expenses : {summary['count']}")
        print(f"Total spent        : ₹{summary['total']:.2f}")

        if summary["highest"]:
            highest = summary["highest"]
            print(
                "Highest expense     : "
                f"₹{highest['amount']:.2f} - "
                f"{highest['category']} ({highest['description']})"
            )

        print("\nCategory totals:")
        if summary["category_totals"]:
            for category, amount in summary["category_totals"].items():
                print(f"  {category:<15} ₹{amount:.2f}")
        else:
            print("  No expenses recorded.")

        print("\nBudget:")
        print(f"  {budget_manager.budget_status(summary['total'])}")
        print("=====================================\n")
