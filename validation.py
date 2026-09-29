from datetime import datetime


ALLOWED_CATEGORIES = {
    "Food",
    "Transport",
    "Education",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Other",
}


def validate_amount(value):
    try:
        amount = float(value)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a valid number.")

    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    return round(amount, 2)


def validate_category(category):
    category = str(category).strip().title()

    if category not in ALLOWED_CATEGORIES:
        raise ValueError(
            "Invalid category. Choose from: "
            + ", ".join(sorted(ALLOWED_CATEGORIES))
        )

    return category


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

    return date_text


def validate_description(description):
    description = str(description).strip()

    if not description:
        raise ValueError("Description cannot be empty.")

    return description
