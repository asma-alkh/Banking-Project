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
            with open(self.bank_file, mode= "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account_id = int(row["account_id"])
                    customer[account_id] = Customer(
                        account_id,
                        row["first_name"],
                        row["last_name"],
                        row["password"],
                        float(row["balance_checking"]),
                        float(row["balance_savings"])
                    )