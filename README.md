# Banking System - Mini Project

A simple and interactive console-based Banking System created using Python. This project simulates essential banking operations such as account creation, login authentication, balance inquiry, deposit, withdrawal, money transfer between accounts, and transaction logging.

---

## 📌 Project Overview

This project is developed using core Python fundamentals. It provides a menu-driven interface where users can easily register for an account, log in securely with their account number and 4-digit PIN, and perform everyday banking tasks.

---

## 🚀 Features

1. **Create Account**:
   - Enter account holder's name, 10-digit phone number, and a 4-digit PIN.
   - Enter initial deposit amount.
   - Generates a unique 5-digit Account Number automatically.

2. **Login System**:
   - Secure login using Account Number and 4-digit PIN.

3. **Check Balance**:
   - View current account balance along with holder details.

4. **Deposit Money**:
   - Add money to your account and get an updated balance.

5. **Withdraw Money**:
   - Withdraw funds with automatic balance validation to prevent overdrafts.

6. **Transfer Money**:
   - Send funds directly to another registered account number.
   - Updates balances and transaction logs for both sender and receiver.

7. **Transaction History**:
   - View a complete statement of all deposits, withdrawals, and transfers with exact date and timestamps.

8. **Change PIN**:
   - Update security PIN by verifying the current PIN and confirming the new one.

9. **Logout**:
   - Safely end current account session and return to the main menu.

---

## 💻 Python Concepts Used

- **Variables & Data Types**: Strings, integers, floats, and booleans.
- **Conditional Statements**: `if`, `elif`, `else` for input validation and menu decisions.
- **Loops**: `while` loops for continuous menu navigation and `for` loops for listing transactions.
- **Functions**: Modular functions for every banking action (`create_account`, `login`, `check_balance`, etc.).
- **Lists & Dictionaries**: In-memory database using a dictionary of accounts with nested transaction lists.
- **String Operations**: Formatted f-strings, `.strip()`, `.isdigit()`, and string slicing/length checks.
- **Modules**:
  - `random`: Used to generate unique 5-digit account numbers.
  - `datetime`: Used to record precise timestamps for all transactions.

---

## 🛠️ How to Run

1. Make sure Python (version 3.6 or higher) is installed on your computer.
2. Open your terminal or command prompt.
3. Navigate to the project folder:
   ```bash
   cd banking-system-project
   ```
4. Run the script:
   ```bash
   python banking_system.py
   ```

---

## 👤 Sample Accounts for Quick Testing

For easy testing without having to create multiple accounts first, two sample accounts are pre-configured:

| Account Number | Account Holder | PIN  | Initial Balance |
|:--------------:|:--------------:|:----:|:---------------:|
| **10001**      | Rahul Sharma   | 1234 | Rs. 5000.00     |
| **10002**      | Priya Singh    | 4321 | Rs. 3000.00     |

---

## 📤 Steps to Push to GitHub

To submit this project on GitHub as required:

1. Initialize git in this folder:
   ```bash
   git init
   ```
2. Add the files:
   ```bash
   git add .
   ```
3. Commit the changes:
   ```bash
   git commit -m "Initial commit - Banking System Mini Project"
   ```
4. Create a new repository on your GitHub account (e.g. named `banking-system-project`).
5. Link your local repo to GitHub and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
