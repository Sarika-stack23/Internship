import json
import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            expense = {
                "date": str(datetime.date.today()),
                "amount": amount,
                "category": category,
                "description": description
            }
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for exp in self.expenses:
            print(f"{exp['date']} - {exp['category']}: ${exp['amount']} ({exp['description']})")

    def category_summary(self):
        summary = {}
        for exp in self.expenses:
            summary[exp['category']] = summary.get(exp['category'], 0) + exp['amount']
        print("Category-wise Summary:")
        for category, amount in summary.items():
            print(f"{category}: ${amount:.2f}")

    def monthly_summary(self):
        monthly = {}
        for exp in self.expenses:
            month = exp['date'][:7]  # Extract YYYY-MM format
            monthly[month] = monthly.get(month, 0) + exp['amount']
        print("Monthly Summary:")
        for month, amount in monthly.items():
            print(f"{month}: ${amount:.2f}")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., Food, Transport, Entertainment): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.category_summary()
        elif choice == "4":
            tracker.monthly_summary()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
