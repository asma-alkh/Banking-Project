class Customer:
    def __init__(self, account_id, first_name, last_name, password):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.balance_checking = float(balance_checking)
        self.balance_savings = float(balance_savings)

# Deposit into checking account
    def deposit_checking(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance_checking += amount