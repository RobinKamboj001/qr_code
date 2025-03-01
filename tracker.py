import json

# File to store expenses
EXPENSE_FILE = "expenses.json"

# Function to load expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add an expense
def add_expense():
    date = input("📅 Enter Date (YYYY-MM-DD): ")
    category = input("🏷️ Enter Category (Food, Transport, Shopping, etc.): ")
    amount = float(input("💰 Enter Amount: "))

    expense = {"date": date, "category": category, "amount": amount}
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense Added Successfully!\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("⚠️ No expenses recorded yet!\n")
        return

    print("\n📜 Your Expenses:")
    total = 0
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']}: ₹{exp['amount']}")
        total += exp["amount"]
    
    print(f"\n💵 Total Expenses: ₹{total}\n")

# Function to show menu
def show_menu():
    while True:
        print("📊 Expense Tracker Menu:")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Exit")

        choice = input("👉 Enter your choice (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("🚪 Exiting Expense Tracker. Have a great day! 😊")
            break
        else:
            print("⚠️ Invalid choice! Please try again.\n")

# Load existing expenses
expenses = load_expenses()

# Start the app
show_menu()
