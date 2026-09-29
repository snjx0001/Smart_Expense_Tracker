import csv
from pathlib import Path


FIELDS = ["amount", "category", "description", "date"]


class Storage:
    """Save and load expense records using a CSV file."""

    def __init__(self, file_path="data/expenses.csv"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, expenses):
        with self.file_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(expenses)

    def load(self):
        if not self.file_path.exists():
            return []

        records = []
        with self.file_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not row:
                    continue
                records.append(
                    {
                        "amount": round(float(row["amount"]), 2),
                        "category": row["category"],
                        "description": row["description"],
                        "date": row["date"],
                    }
                )

        return records
