import csv
from account import BankAccount

def load_accounts(file_path):
    accounts = {}
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = BankAccount(
                    row['account_id'],
                    row['frst_name'],
                    row['last_name'],
                    row['password'],
                    row['balance_checking'],
                    row['balance_savings']
                )
                accounts[row['account_id']] = account
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    return accounts

if __name__ == "__main__":
    accounts = load_accounts("bank.csv")
    for acc_id, acc in accounts.items():
        print(f"Account ID: {acc.account_id}")
        print(f"First Name: {acc.first_name}")
        print(f"Last Name: {acc.last_name}")
        print(f"Checking Balance: {acc.balance_checking}")
        print(f"Savings Balance: {acc.balance_savings}")
        print("-" * 30)
