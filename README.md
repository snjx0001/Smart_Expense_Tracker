# Smart Expense Tracker

This is my Python Essentials course project. It is a simple expense tracker that stores expense records in a CSV file and lets the user manage them from either the command line or a Jupyter Notebook.

## What the project can do

- Add an expense
- View saved expenses
- Update an expense
- Delete an expense
- Search by category or description
- Show total spending and category totals
- Set a monthly budget
- Show remaining budget
- Save and load expenses using CSV
- Validate common inputs
- Run automated tests

## Project files

```text
Smart_Expense_Tracker/
├── data/
│   └── expenses.csv
├── diagrams/
├── expense_tracker.ipynb
├── main.py
├── expense_manager.py
├── budget_manager.py
├── reports.py
├── storage.py
├── validation.py
├── dashboard.py
├── test_expense_tracker.py
├── README.md
├── statement.md
└── requirements.txt
```

## Requirements

- Python 3.9 or newer
- Jupyter Notebook or JupyterLab only if you want to use the notebook version
- No third-party Python packages are needed for the command-line program

## Run from the command line

Open a terminal in the project folder and run:

```bash
python main.py
```

The program shows this menu:

```text
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
```

## Run in Jupyter Notebook

Open `expense_tracker.ipynb` and run the cells in order. The last application cell starts the same expense tracker menu.

## Data storage

Expenses are stored in:

```text
data/expenses.csv
```

The CSV columns are:

```text
amount,category,description,date
```

## Run the tests

```bash
python -m unittest test_expense_tracker.py -v
```

The test file checks expense operations, validation, budget calculations, reports, date filtering, search, and CSV storage.

## Main modules

- `expense_manager.py` - expense operations
- `budget_manager.py` - budget calculations
- `reports.py` - summaries and reports
- `storage.py` - CSV save/load
- `validation.py` - input checks
- `dashboard.py` - expense summary, category totals, and budget status
- `main.py` - command-line program
- `expense_tracker.ipynb` - notebook version
- `test_expense_tracker.py` - automated tests

## Current limitations

- The monthly budget is kept only for the current run of the program.
- Data is stored locally in a CSV file.
- There is no login system or online synchronization.
- The interface is text based.

## Possible future improvements

- Charts for spending categories
- Category-specific budgets
- Monthly and yearly comparisons
- Database storage
- PDF report export
- A graphical user interface
