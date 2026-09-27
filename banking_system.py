# Banking System - Mini Project
# Simple Python Console Application for Basic Banking Operations

import random
import datetime

# Dictionary to store all bank accounts
# Account Number is used as the key
accounts = {
    "10001": {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": [
            "[2026-09-20 10:00:00] Account opened with initial deposit: Rs. 5000.00"
        ]
    },
    "10002": {
        "name": "Priya Singh",
        "phone": "9123456780",
        "pin": "4321",
        "balance": 3000.0,
        "transactions": [
            "[2026-09-20 10:15:00] Account opened with initial deposit: Rs. 3000.00"
        ]
    }
}


# Helper function to get current formatted date and time
def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Helper function to generate a unique 5-digit account number
def generate_account_number():
    while True:
        acc_num = str(random.randint(10000, 99999))
        if acc_num not in accounts:
            return acc_num


# Feature 1: Create a new bank account
def create_account():
    print("\n---------------------------------")
    print("       CREATE NEW ACCOUNT")
    print("---------------------------------")
    
    name = input("Enter your full name: ").strip()
    if name == "":
        print("Error: Name cannot be empty!")
        return

    phone = input("Enter your 10-digit phone number: ").strip()
    if len(phone) != 10 or not phone.isdigit():
        print("Error: Please enter a valid 10-digit phone number!")
        return

    pin = input("Create a 4-digit PIN: ").strip()
    if len(pin) != 4 or not pin.isdigit():
        print("Error: PIN must be exactly 4 digits!")
        return

    # Take initial deposit amount
    try:
        initial_deposit = float(input("Enter initial deposit amount (Rs.): "))
        if initial_deposit < 0:
            print("Error: Initial deposit cannot be negative!")
            return
    except ValueError:
        print("Error: Please enter a valid number for amount!")
        return

    # Generate account number and save details in dictionary
    acc_num = generate_account_number()
    time_stamp = get_current_time()
    
    accounts[acc_num] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": initial_deposit,
        "transactions": [
            f"[{time_stamp}] Account opened with initial deposit: Rs. {initial_deposit:.2f}"
        ]
    }

    print("\n>>> Account Created Successfully! <<<")
    print(f"Account Holder : {name}")
    print(f"Account Number : {acc_num}")
    print(f"Initial Balance: Rs. {initial_deposit:.2f}")
    print("Please remember your Account Number and PIN to log in.")


# Feature 2: Login using Account Number and PIN
def login():
    print("\n---------------------------------")
    print("             LOGIN")
    print("---------------------------------")
    
    acc_num = input("Enter your Account Number: ").strip()
    pin = input("Enter your 4-digit PIN: ").strip()

    if acc_num in accounts and accounts[acc_num]["pin"] == pin:
        print(f"\nLogin successful! Welcome, {accounts[acc_num]['name']}.")
        account_menu(acc_num)
    else:
        print("\nError: Invalid Account Number or PIN. Please try again!")


# Feature 3: Check Account Balance
def check_balance(acc_num):
    print("\n---------------------------------")
    print("         ACCOUNT BALANCE")
    print("---------------------------------")
    print(f"Account Holder : {accounts[acc_num]['name']}")
    print(f"Account Number : {acc_num}")
    print(f"Current Balance: Rs. {accounts[acc_num]['balance']:.2f}")


# Feature 4: Deposit Money
def deposit_money(acc_num):
    print("\n---------------------------------")
    print("          DEPOSIT MONEY")
    print("---------------------------------")
    
    try:
        amount = float(input("Enter amount to deposit (Rs.): "))
        if amount <= 0:
            print("Error: Deposit amount must be greater than 0!")
            return

        accounts[acc_num]["balance"] += amount
        time_stamp = get_current_time()
        
        # Add to transaction history
        record = f"[{time_stamp}] Deposited: +Rs. {amount:.2f} | Balance: Rs. {accounts[acc_num]['balance']:.2f}"
        accounts[acc_num]["transactions"].append(record)

        print(f"\nRs. {amount:.2f} deposited successfully.")
        print(f"Updated Balance: Rs. {accounts[acc_num]['balance']:.2f}")

    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only!")


# Feature 5: Withdraw Money
def withdraw_money(acc_num):
    print("\n---------------------------------")
    print("         WITHDRAW MONEY")
    print("---------------------------------")
    
    try:
        amount = float(input("Enter amount to withdraw (Rs.): "))
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than 0!")
            return

        current_balance = accounts[acc_num]["balance"]
        if amount > current_balance:
            print(f"Error: Insufficient balance! Your current balance is Rs. {current_balance:.2f}")
            return

        accounts[acc_num]["balance"] -= amount
        time_stamp = get_current_time()

        # Add to transaction history
        record = f"[{time_stamp}] Withdrew: -Rs. {amount:.2f} | Balance: Rs. {accounts[acc_num]['balance']:.2f}"
        accounts[acc_num]["transactions"].append(record)

        print(f"\nRs. {amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: Rs. {accounts[acc_num]['balance']:.2f}")

    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only!")


# Feature 6: Transfer Money between accounts
def transfer_money(acc_num):
    print("\n---------------------------------")
    print("         TRANSFER MONEY")
    print("---------------------------------")
    
    receiver_acc = input("Enter receiver's Account Number: ").strip()

    if receiver_acc == acc_num:
        print("Error: You cannot transfer money to your own account!")
        return

    if receiver_acc not in accounts:
        print("Error: Receiver account not found. Please check the account number!")
        return

    try:
        amount = float(input("Enter amount to transfer (Rs.): "))
        if amount <= 0:
            print("Error: Transfer amount must be greater than 0!")
            return

        sender_balance = accounts[acc_num]["balance"]
        if amount > sender_balance:
            print(f"Error: Insufficient balance! Your balance is Rs. {sender_balance:.2f}")
            return

        # Deduct from sender
        accounts[acc_num]["balance"] -= amount
        time_stamp = get_current_time()
        sender_record = f"[{time_stamp}] Transferred to Acc {receiver_acc} ({accounts[receiver_acc]['name']}): -Rs. {amount:.2f} | Balance: Rs. {accounts[acc_num]['balance']:.2f}"
        accounts[acc_num]["transactions"].append(sender_record)

        # Add to receiver
        accounts[receiver_acc]["balance"] += amount
        receiver_record = f"[{time_stamp}] Received from Acc {acc_num} ({accounts[acc_num]['name']}): +Rs. {amount:.2f} | Balance: Rs. {accounts[receiver_acc]['balance']:.2f}"
        accounts[receiver_acc]["transactions"].append(receiver_record)

        print(f"\nTransfer successful! Sent Rs. {amount:.2f} to {accounts[receiver_acc]['name']} (Acc: {receiver_acc}).")
        print(f"Your Remaining Balance: Rs. {accounts[acc_num]['balance']:.2f}")

    except ValueError:
        print("Error: Invalid amount entered. Please enter numbers only!")


# Feature 7: View Transaction History
def view_transaction_history(acc_num):
    print("\n---------------------------------")
    print("       TRANSACTION HISTORY")
    print("---------------------------------")
    
    transactions = accounts[acc_num]["transactions"]
    if len(transactions) == 0:
        print("No transactions found.")
        return

    print(f"Account: {acc_num} | Name: {accounts[acc_num]['name']}")
    print("-" * 55)
    for index, item in enumerate(transactions, start=1):
        print(f"{index}. {item}")
    print("-" * 55)


# Feature 8: Change PIN
def change_pin(acc_num):
    print("\n---------------------------------")
    print("           CHANGE PIN")
    print("---------------------------------")
    
    old_pin = input("Enter your old PIN: ").strip()
    if old_pin != accounts[acc_num]["pin"]:
        print("Error: Incorrect old PIN!")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Error: New PIN must be exactly 4 digits!")
        return

    confirm_pin = input("Confirm new PIN: ").strip()
    if new_pin != confirm_pin:
        print("Error: PIN confirmation does not match!")
        return

    # Update PIN
    accounts[acc_num]["pin"] = new_pin
    time_stamp = get_current_time()
    accounts[acc_num]["transactions"].append(f"[{time_stamp}] PIN was changed successfully")
    print("\nPIN has been changed successfully!")


# Account Menu after successful login
def account_menu(acc_num):
    while True:
        print("\n=================================")
        print(f"  ACCOUNT MENU ({accounts[acc_num]['name']})")
        print("=================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("=================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(acc_num)
        elif choice == "2":
            deposit_money(acc_num)
        elif choice == "3":
            withdraw_money(acc_num)
        elif choice == "4":
            transfer_money(acc_num)
        elif choice == "5":
            view_transaction_history(acc_num)
        elif choice == "6":
            change_pin(acc_num)
        elif choice == "7":
            print("\nLogging out... Returning to Main Menu.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


# Main Menu loop
def main():
    while True:
        print("\n=================================")
        print("    BANKING SYSTEM - MAIN MENU")
        print("=================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("=================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("\nThank you for using the Banking System. Have a great day!")
            break
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")


# Program entry point
if __name__ == "__main__":
    main()
