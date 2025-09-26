import csv 
from bank.customer import Customer
from bank.transction import Transction 

class BankSystem:

    def __init__(self, bank_file="bank.csv", transaction_file="transactions.csv"):
        self.bank_file = bank_file
        self.transaction_file = transaction_file
        self.customers = self.load_customers()
        self.transactions = []
        self.transction_counter = 1

    def load_customers(self):
        customers = {}
        try:
            with open(self.bank_file, mode="r") as file:  
                reader = csv.DictReader(file)
                for row in reader:
                    account_id = int(row["account_id"])
                    customers[account_id] = Customer( 
                        account_id,
                        row["first_name"],
                        row["last_name"],
                        row["password"],
                        float(row["balance_checking"]),
                        float(row["balance_savings"])
                    )

        except FileNotFoundError:
            print("Bank file not found. Starting with empty customer list.")
        return customers

    def save_customers(self):
        with open(self.bank_file, mode="w",newline="") as file:
            fieldnames = ["account_id", "first_name",
                      "last_name", "password",
                      "balance_checking", "balance_savings"]
            writer = csv.DictWriter(file,fieldnames = fieldnames)
            writer.writeheader()
            for cust in self.customers.values(): 
                writer.writerow({
                    "account_id": cust.account_id,
                    "first_name": cust.first_name, 
                    "last_name": cust.last_name,
                    "password": cust.password,
                    "balance_checking": cust.checking_account.get_balance() if cust.has_checking() else 0.0,
                    "balance_savings": cust.savings_account.get_balance() if cust.has_savings() else 0.0,
                })                  

    def add_customer(self, first_name, last_name, password, with_checking=True, with_savings=False):
        new_id = max(self.customers.keys(), default=10000) + 1
        checking_balance = 0.0 if with_checking else None 
        savings_balance = 0.0 if with_savings else None 
        customer - Customer(new_id, first_name, last_name, password, checking_balance, savings_balance) 

        self.customers[new_id] = customer 
        self.save_customers()
        return customer     