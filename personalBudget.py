import json
import os

# File path for storing transactions
TRANSACTIONS_FILE = "transactions.json"

# Function to load transactions from file
def load_transactions():
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as file:
            return json.load(file)
    else:
        return {"income": [], "expenses": []}

# Function to save transactions to file
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file)

# Function to add income
def add_income(transactions):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    transactions["income"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Income added successfully.")

# Function to add expense
def add_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Expense added successfully.")

# Function to calculate remaining budget
def calculate_budget(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions["income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to analyze expenses
def analyze_expenses(transactions):
    expenses_by_category = {}
    for transaction in transactions["expenses"]:
        category = transaction["category"]
        amount = transaction["amount"]
        expenses_by_category[category] = expenses_by_category.get(category, 0) + amount
    print("Expense Analysis:")
    for category, amount in expenses_by_category.items():
        print(f"- {category}: ${amount:.2f}")

# Main function
def main():
    transactions = load_transactions()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_income(transactions)
        elif choice == '2':
            add_expense(transactions)
        elif choice == '3':
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == '4':
            analyze_expenses(transactions)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
