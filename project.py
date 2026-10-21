import json
from datetime import datetime

filename = "samplerecord.json"


def load_expenses(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses, filename):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses, amount, category, date, note=""):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    expense = {"amount": amount,
               "category": category,
               "date": date.isoformat(),
               "note": note}
    expenses.append(expense)
    return expenses


def delete_expense(expenses, index):
    if index < 0 or index >= len(expenses):
        raise ValueError("Invalid index")
    expenses.pop(index)
    return expenses


def total_spent(expenses):
    return sum(expense["amount"] for expense in expenses)


def total_by_cat(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0)+expense["amount"]
    return totals


def main():
    expenses = load_expenses(filename)

    while True:
        print("-------------EXPENSES TRACKER-------------")
        print("1. Expenses\n"
              "2. Save the expenses\n"
              "3. Add expenses\n"
              "4. Delete expense\n"
              "5. Total Expense\n"
              "6. Total expense by category\n"
              "7. Exit\n")
        print("-------------***-------------")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 7.")
            continue

        match choice:
            case 1:
                if not expenses:
                    print("No expenses yet")
                else:
                    for number, expense in enumerate(expenses, start=1):
                        print(
                            f"{number}. {expense['amount']} | {expense['category']} | {expense['date']} | {expense['note']}")

            case 2:
                save_expenses(expenses, filename)
                print("expenses saved")
            case 3:
                try:
                    amount = float(input("Enter your expense: "))
                    category = input("Enter the category: ")
                    date_input = input("Enter date (DD-MM-YYYY): ")
                    date = datetime.strptime(date_input, "%d-%m-%Y").date()
                    note = input("Enter a note: ")

                    expenses = add_expense(
                        expenses, amount, category, date, note)
                    save_expenses(expenses, filename)
                    print("Expense added.")
                except ValueError as e:
                    print("Invalid input", e)
            case 4:
                if not expenses:
                    print("No expenses to delete")
                else:
                    try:
                        for number, expense in enumerate(expenses, start=1):
                            print(
                                f"{number}. {expense['amount']} | {expense['category']} | {expense['date']} | {expense['note']}")
                        number = int(
                            input("Enter the expense number you want to delete: "))
                        sure = input(
                            f"Do you wanna delete the contents of {number}?(Y/N)").upper()
                        if sure == 'Y':
                            expenses = delete_expense(expenses, number-1)
                            save_expenses(expenses, filename)
                            print(f"Expense {number} successfully deleted.")
                        else:
                            print("Your file didn't delete any expense.")
                    except ValueError as e:
                        print("Invalid input", e)
            case 5:
                total = total_spent(expenses)
                print(f"Your total expense is ₹{total:.2f}")

            case 6:
                if not expenses:
                    print("No expenses yet.")
                else:
                    totals = total_by_cat(expenses)
                    for category, amount in totals.items():
                        print(f"{category}: ₹{amount:.2f}")
            case 7:
                user = input(
                    "Do you wanna exit the Expense tracker?(Y/N)").upper()
                if user == 'Y':
                    break
            case _:
                print("Invalid choice")


if __name__ == '__main__':
    main()
