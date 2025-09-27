## 🏦 Bank System

A simple **command-line banking system** built in python.
This project allows customers to log in, check their account balance, deposit, withdraw, and transfer money between accounts.

---

## 🚀 Features 
- Customers login with account ID and password
- Checking and savings accounts 
- Deposit & withdraw money 
- Transfer between accounts or to another customer
- Data loaded from CSV file 
- Includes unit from main functions

---

## 🖥️ Installation & Run

Clone the project and run:

```bash
python main.py
```
## Usage  

Once you run the program, you can:

- **Log in** with an existing account ID and password 
- **View available operations** (deposit, withdraw, transfer, check balance)
-**Perform transactions** and instantly see the updated balances


## 💡 Code I Am Proud Of

def withdraw(self, customer, account_type, amount):
    # Get the right account (checking or savings)
    account = customer.get_account(account_type)
    if not account:
        return False, "Account type not found"

    if amount <= 0:
        return False, "Invalid amount"

    if account.get_balance() - amount < account.overdraft_limit:
        return False, "Withdrawal denied: would exceed overdraft limit"

    account.balance -= amount
    return True, "Withdrawal successful"

This function:
- ✅ Selects the correct account (checking or savings).
- ✅ Validates that the amount is positive.
- ✅ Prevents overdrawing below the allowed limit.
- ✅ Updates the balance only if the withdrawal is safe.

---

## 📚 What I Learned
- How to organize a Python project using multiple files and classes
- How to store and read data from CSV files
- How to use unit testing (unittest) to check if my code works correctly
- How to build a simple command-line interface (CLI)

---

## ⚠️ Challenges I Faced
- Understanding how to link different classes together (BankSystem ↔ Customer ↔ Accounts)
- Designing the withdraw/transfer logic so that it is safe and handles errors correctly
- Making sure deposits, withdrawals, and transfers always keep balances accurate