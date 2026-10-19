import json
import random
from pathlib import Path


class Bank:
    database = "data.json"

    def __init__(self):
        self.data = []

        try:
            if Path(self.database).exists():
                with open(self.database, "r") as fs:
                    self.data = json.load(fs)
            else:
                print("No such data exists. New database created.")

        except (json.JSONDecodeError, OSError) as err:
            print(f"Error loading database: {err}")

    def update(self):
        try:
            with open(self.database, "w") as fs:
                json.dump(self.data, fs, indent=4)
        except OSError as err:
            print(f"Error saving data: {err}")

    def find_account(self, account_no):
        for account in self.data:
            if account["account_no"] == account_no:
                return account
        return None

    def createaccount(self):
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            pin = input("Enter your 4-digit PIN: ")

            if age < 18:
                print("You are a minor. Account cannot be created.")
                return

            if len(pin) != 4 or not pin.isdigit():
                print("PIN must contain exactly 4 digits.")
                return

            account_no = random.randint(100000, 999999)

            while self.find_account(account_no) is not None:
                account_no = random.randint(100000, 999999)

            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": pin,
                "account_no": account_no,
                "balance": 0
            }

            self.data.append(info)
            self.update()

            print("\nAccount created successfully!")
            print(f"Account Number: {account_no}")
            print(f"Name: {name}")
            print("Please note down your account number.")

        except ValueError:
            print("Please enter a valid age.")

    def deposit(self):
        try:
            account_no = int(input("Enter account number: "))
            account = self.find_account(account_no)

            if account is None:
                print("Account not found.")
                return

            amount = float(input("Enter deposit amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            account["balance"] += amount
            self.update()

            print(f"Deposit successful! Balance: {account['balance']:.2f}")

        except ValueError:
            print("Please enter valid numbers.")

    def withdraw(self):
        try:
            account_no = int(input("Enter account number: "))
            account = self.find_account(account_no)

            if account is None:
                print("Account not found.")
                return

            pin = input("Enter your PIN: ")

            if pin != account["pin"]:
                print("Incorrect PIN.")
                return

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > account["balance"]:
                print("Insufficient balance.")
            else:
                account["balance"] -= amount
                self.update()
                print(
                    f"Withdrawal successful! "
                    f"Balance: {account['balance']:.2f}"
                )

        except ValueError:
            print("Please enter valid numbers.")

    def details(self):
        try:
            account_no = int(input("Enter account number: "))
            account = self.find_account(account_no)

            if account is None:
                print("Account not found.")
                return

            pin = input("Enter your PIN: ")

            if pin != account["pin"]:
                print("Incorrect PIN.")
                return

            print("\n--- Account Details ---")
            for key, value in account.items():
                if key != "pin":
                    print(f"{key}: {value}")

        except ValueError:
            print("Please enter a valid account number.")

    def update_details(self):
        try:
            account_no = int(input("Enter account number: "))
            account = self.find_account(account_no)

            if account is None:
                print("Account not found.")
                return

            pin = input("Enter your PIN: ")

            if pin != account["pin"]:
                print("Incorrect PIN.")
                return

            name = input("Enter new name (Enter to skip): ")
            email = input("Enter new email (Enter to skip): ")

            if name.strip():
                account["name"] = name

            if email.strip():
                account["email"] = email

            self.update()
            print("Account details updated successfully.")

        except ValueError:
            print("Please enter a valid account number.")

    def delete_account(self):
        try:
            account_no = int(input("Enter account number: "))
            account = self.find_account(account_no)

            if account is None:
                print("Account not found.")
                return

            pin = input("Enter your PIN: ")

            if pin != account["pin"]:
                print("Incorrect PIN.")
                return

            confirm = input("Type YES to delete account: ")

            if confirm == "YES":
                self.data.remove(account)
                self.update()
                print("Account deleted successfully.")
            else:
                print("Account deletion cancelled.")

        except ValueError:
            print("Please enter a valid account number.")


# Main program
bank = Bank()

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Update Details")
    print("6. Delete Account")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            bank.createaccount()
        elif choice == 2:
            bank.deposit()
        elif choice == 3:
            bank.withdraw()
        elif choice == 4:
            bank.details()
        elif choice == 5:
            bank.update_details()
        elif choice == 6:
            bank.delete_account()
        elif choice == 7:
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Please select 1 to 7.")

    except ValueError:
        print("Please enter a valid menu number.")