import datetime

class Transaction:
    def __init__(self, transaction_id, account_id, transaction_type,
                 amount, from_account, to_account, balance_after):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account
        self.balance_after = balance_after
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")