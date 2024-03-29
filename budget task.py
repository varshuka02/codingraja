#BUDGET
import json

def load_budget_data():
    try:
        with open("budget.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "income": 0,
            "expenses": []
        }

budget = load_budget_data()

def show_menu():
    print("Budget Tracker Menu")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def add_income():
    try:
        amount = float(input("Enter the income amount: "))
        budget["income"] += amount
        print(f"Income of ${amount} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_expense():
    category = input("Enter the expense category: ")
    try:
        amount = float(input("Enter the expense amount: "))
        budget["expenses"].append({"category": category, "amount": amount})
        print(f"Expense of ${amount} in {category} added successfully!")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_budget():
    total_expenses = sum(item["amount"] for item in budget["expenses"])
    remaining_budget = budget["income"] - total_expenses
    return remaining_budget

def view_expense_analysis():
    categories = set(item["category"] for item in budget["expenses"])
    print("Expense Analysis:")
    for category in categories:
        total_category_expense = sum(item["amount"] for item in budget["expenses"] if item["category"] == category)
        print(f"{category}: ${total_category_expense}")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        remaining_budget = calculate_budget()
        print(f"Remaining Budget: ${remaining_budget}")
    elif choice == "4":
        view_expense_analysis()
    elif choice == "5":
        with open("budget.json", "w") as file:
            json.dump(budget, file)
        print("Budget data saved. Exiting...")
        break
    else:
        print("Invalid choice. Please select a valid option.")