# Smart Expense Tracker - Project Statement

## Project Title

**Smart Expense Tracker**

## Problem Statement

Managing day-to-day expenses manually can make it difficult to understand spending patterns, track a budget, and retrieve previous transactions. Smart Expense Tracker provides a simple Python-based system for recording, storing, managing, and summarizing personal expenses.

## Scope

The project includes:

- Adding, viewing, updating, and deleting expenses
- Searching expenses by category or description
- Calculating total spending
- Setting and checking a monthly budget
- Displaying expense summaries and category totals
- Saving and loading expenses using CSV
- Validating user input and handling errors
- Automated unit testing
- Command-line and Jupyter Notebook interfaces

The project does not include online banking integration, payment processing, or cloud synchronization.

## Target Users

- Students tracking daily spending
- Individuals managing personal expenses
- Beginners who want a simple budgeting tool
- Python learners studying modular application development

## Objectives

1. Build a practical application using Python Essentials concepts.
2. Implement CRUD operations for expense records.
3. Store data permanently with CSV file handling.
4. Apply modular programming with separate Python files.
5. Validate inputs and handle errors safely.
6. Track spending against a user-defined budget.
7. Generate useful summaries and reports.
8. Test important functionality using `unittest`.

## Functional Requirements

The system should allow users to:

1. Add an expense with amount, category, description, and date.
2. View stored expenses.
3. Update an expense.
4. Delete an expense.
5. Search expenses by category or description.
6. View total spending and summaries.
7. Set a monthly budget.
8. View remaining budget or budget-exceeded status.
9. Save expense information to CSV.
10. Load saved expense information.
11. Generate expense summaries and category totals through the reporting module.

## Non-Functional Requirements

### Usability
The interface should use clear menus, prompts, and readable output.

### Reliability
Saved expense records should be loaded consistently between sessions.

### Maintainability
Functionality should be divided into separate modules with clear responsibilities.

### Data Integrity
Amounts, categories, descriptions, and dates should be validated before being accepted by the command-line application and notebook interface.

### Portability
The core application should run on Python 3 without third-party dependencies.

## Technology Used

- Python 3
- Jupyter Notebook
- CSV file handling
- Python `unittest`
- Object-oriented programming
- Git and GitHub

## Expected Outcome

The final result is a working, modular personal expense tracker that can be executed from the command line, demonstrated in Jupyter Notebook, tested automatically, and stored in a public GitHub repository.
