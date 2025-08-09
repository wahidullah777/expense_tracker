import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize the file if it doesn't exist
if not os.path.isfile(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount: ")
    note = input("Enter a short note: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("✅ Expense added!")

def view_expenses():
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet.")
        return

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def menu():
    while True:
        print("\n📊 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice (1-3): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
