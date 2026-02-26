import datetime
import json
import os
import uuid
from json import JSONDecodeError


class FinanceManager:
    def __init__(self, file_path="expense.json"):
        self.file_path = file_path
        self.categories = ["Food", "Transport", "Utils"]
        self.expenses = {}

        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.expenses = json.load(f)
            except JSONDecodeError:
                self.expenses = {}

    # ---------- INTERNAL SAVE METHOD ----------
    def _save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.expenses, f, indent=4)

    # ---------- ADD EXPENSE ----------
    def add_expense(self):
        try:
            expense_id = str(uuid.uuid4())

            amount = int(input("Enter price of expense: "))
            while amount <= 0:
                amount = int(input("Enter a positive amount: "))

            ctg = input("Enter category (Food, Transport, Utils): ").capitalize()
            while ctg not in self.categories:
                ctg = input("Invalid category. Enter again: ").capitalize()

            description = input("Enter description: ")

            date = datetime.datetime.now().strftime("%m/%d/%Y")

            expense = {
                "amount": amount,
                "category": ctg,
                "description": description,
                "date": date
            }

            self.expenses[expense_id] = expense
            self._save()

            print("Expense added successfully.")

        except ValueError:
            print("Invalid input.")

    # ---------- DELETE ALL ----------
    def delete_all_expenses(self):
        self.expenses.clear()
        self._save()
        print("All expenses deleted.")

    # ---------- DELETE BY ID ----------
    def delete_expense_by_id(self, expense_id):
        if expense_id in self.expenses:
            del self.expenses[expense_id]
            self._save()
            print("Expense deleted.")
        else:
            print("Expense ID not found.")

    # ---------- EDIT ----------
    def edit_expense(self, expense_id, amount=None, description=None, ctg=None):
        if expense_id not in self.expenses:
            print("Expense ID not found.")
            return

        if amount is not None:
            self.expenses[expense_id]["amount"] = amount

        if description is not None:
            self.expenses[expense_id]["description"] = description

        if ctg is not None and ctg in self.categories:
            self.expenses[expense_id]["category"] = ctg

        self._save()
        print("Expense updated.")

    # ---------- FILTER ----------
    def filter_by_category(self, category):
        return {
            exp_id: exp
            for exp_id, exp in self.expenses.items()
            if exp["category"] == category
        }

    # ---------- MONTHLY SUMMARY ----------
    def monthly_summary(self):
        summary = {}
        for exp in self.expenses.values():
            month = exp["date"][:2] + "/" + exp["date"][-4:]
            summary[month] = summary.get(month, 0) + exp["amount"]
        return summary

    # ---------- HIGHEST EXPENSE ----------
    def show_highest_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses.items(), key=lambda x: x[1]["amount"])

    # ---------- TOTAL (Dynamic Calculation) ----------
    def get_total(self):
        return sum(exp["amount"] for exp in self.expenses.values())

if __name__ == "__main__":
    manager = FinanceManager()

    while True:
        print("\n1. Add Expense")
        print("2. Delete Expense by ID")
        print("3. Delete All Expenses")
        print("4. Edit Expense")
        print("5. Show All Expenses")
        print("6. Filter by Category")
        print("7. Monthly Summary")
        print("8. Show Highest Expense")
        print("9. Show Total")
        print("10. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            exp_id = input("Enter Expense ID: ")
            manager.delete_expense_by_id(exp_id)

        elif choice == "3":
            confirm = input("Are you sure you want to delete all expenses? (y/n): ")
            if confirm.lower() == "y":
                manager.delete_all_expenses()

        elif choice == "4":
            exp_id = input("Enter Expense ID to edit: ")

            try:
                amount_input = input("New amount (leave blank to skip): ")
                amount = int(amount_input) if amount_input else None
            except ValueError:
                amount = None

            description = input("New description (leave blank to skip): ") or None

            ctg = input("New category (Food, Transport, Utils) (leave blank to skip): ").capitalize()
            if ctg == "":
                ctg = None

            manager.edit_expense(exp_id, amount, description, ctg)

        elif choice == "5":
            print(manager.expenses)

        elif choice == "6":
            cat = input("Enter category: ").capitalize()
            print(manager.filter_by_category(cat))

        elif choice == "7":
            print(manager.monthly_summary())

        elif choice == "8":
            print(manager.show_highest_expense())

        elif choice == "9":
            print("Total:", manager.get_total())

        elif choice == "10":
            break

        else:
            print("Invalid option.")