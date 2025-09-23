import datetime
from typing import Dict

class Transaction:
    """Transaction class to record all transactions"""
    
    def __init__(self, transaction_id: str, account_id: str, transaction_type: str, 
                 amount: float, from_account: str = "", to_account: str = "", 
                 balance_after: float = 0.0, timestamp: str = None):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account
        self.balance_after = balance_after
        self.timestamp = timestamp or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        """Convert transaction to dictionary for CSV storage"""
        return {
            "transaction_id": self.transaction_id,
            "account_id": self.account_id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "from_account": self.from_account,
            "to_account": self.to_account,
            "balance_after": self.balance_after,
            "timestamp": self.timestamp
        }
    def display_transaction(self):
        """Display transaction details in a formatted way"""
    print(f"\n=== TRANSACTION DETAILS ===")
    print(f"Transaction ID: {self.transaction_id}")
    print(f"Date/Time: {self.timestamp}")
    print(f"Type: {self.transaction_type.upper()}")
    print(f"Amount: ${self.amount:.2f}")
    if self.from_account:
            print(f"From Account: {self.from_account}")
    if self.to_account:
            print(f"To Account: {self.to_account}")
    print(f"Balance After: ${self.balance_after:.2f}")
    print("=" * 3)