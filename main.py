import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_expense(data):
    title = input("Title: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data.append(expense)

    save_data(data)

    print("Expense added")


def show_expenses(data):
    if not data:
        print("No expenses found")
        return

    print()

    for i, expense in enumerate(data, start=1):
        print(f"{i}. {expense['title']}")
        print(f"   Amount   : ₹{expense['amount']}")
        print(f"   Category : {expense['category']}")
        print(f"   Date     : {expense['date']}")
        print()


def total_expense(data):
    total = sum(item["amount"] for item in data)

    print(f"Total Expense: ₹{total}")


def highest_expense(data):
    if not data:
        print("No expenses found")
        return

    highest = max(data, key=lambda x: x["amount"])

    print()
    print("Highest Expense")
    print(f"Title    : {highest['title']}")
    print(f"Amount   : ₹{highest['amount']}")
    print(f"Category : {highest['category']}")


def category_summary(data):
    summary = {}

    for expense in data:
        category = expense["category"]

        if category not in summary:
            summary[category] = 0

        summary[category] += expense["amount"]

    print()

    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")


def search_expense(data):
    keyword = input("Enter keyword: ").lower()

    found = False

    print()

    for expense in data:
        if keyword in expense["title"].lower():
            print(f"{expense['title']} - ₹{expense['amount']}")
            found = True

    if not found:
        print("No matching expense found")


def filter_by_category(data):
    category_name = input("Enter category: ").lower()

    print()

    found = False

    for expense in data:
        if expense["category"].lower() == category_name:
            print(f"{expense['title']} - ₹{expense['amount']}")
            found = True

    if not found:
        print("No expenses in this category")


def delete_expense(data):
    show_expenses(data)

    if not data:
        return

    try:
        choice = int(input("Enter number to delete: ")) - 1

        if 0 <= choice < len(data):
            removed = data.pop(choice)

            save_data(data)

            print(f"{removed['title']} deleted")

        else:
            print("Invalid choice")

    except:
        print("Invalid input")


def update_expense(data):
    show_expenses(data)

    if not data:
        return

    try:
        choice = int(input("Enter number to update: ")) - 1

        if 0 <= choice < len(data):
            expense = data[choice]

            new_title = input("New title: ")
            new_amount = float(input("New amount: "))
            new_category = input("New category: ")

            expense["title"] = new_title
            expense["amount"] = new_amount
            expense["category"] = new_category

            save_data(data)

            print("Expense updated")

        else:
            print("Invalid choice")

    except:
        print("Invalid input")


def menu():
    data = load_data()

    while True:
        print()
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Total Expense")
        print("4. Highest Expense")
        print("5. Category Summary")
        print("6. Search Expense")
        print("7. Filter By Category")
        print("8. Update Expense")
        print("9. Delete Expense")
        print("10. Exit")
        print()

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense(data)

        elif choice == "2":
            show_expenses(data)

        elif choice == "3":
            total_expense(data)

        elif choice == "4":
            highest_expense(data)

        elif choice == "5":
            category_summary(data)

        elif choice == "6":
            search_expense(data)

        elif choice == "7":
            filter_by_category(data)

        elif choice == "8":
            update_expense(data)

        elif choice == "9":
            delete_expense(data)

        elif choice == "10":
            print("Exiting")
            break

        else:
            print("Invalid choice")


menu()