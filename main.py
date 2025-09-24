from typing import Optional, Dict, Tuple
import datetime

class BankAccount:
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id
        self.balance = balance
        self.overdraft_count = 0
        self.is_active = True
        self.overdraft_limit = -100.0
        self.overdraft_fee = 35.0

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def can_withdraw(self, amount: float) -> Tuple[bool, str]:
        if not self.is_active:
            return False, "Account is deactivated"
        if amount <= 0:
            return False, "Invalid withdrawal amount"
        new_balance = self.balance - amount
        if new_balance < self.overdraft_limit:
            return False, f"Would exceed overdraft limit of {self.overdraft_limit}"
        if self.balance < 0 and amount > 100:
            return False, "Cannot withdraw more than $100 when account is negative"
        return True, ""

    def withdraw(self, amount: float) -> Tuple[bool, str]:
        can_withdraw, message = self.can_withdraw(amount)
        if not can_withdraw:
            return False, message
        would_overdraft = (self.balance - amount) < 0 and self.balance >= 0
        self.balance -= amount
        if would_overdraft:
            self.overdraft_count += 1
            self.balance -= self.overdraft_fee
            if self.overdraft_count >= 2:
                self.is_active = False
                return True, f"Withdrawal successful. Overdraft fee of ${self.overdraft_fee} applied. Account deactivated due to 2 overdrafts."
            else:
                return True, f"Withdrawal successful. Overdraft fee of ${self.overdraft_fee} applied. {2 - self.overdraft_count} overdrafts remaining before deactivation."
        return True, "Withdrawal successful"

    def get_balance(self) -> float:
        return self.balance

    def reactivate_account(self) -> bool:
        if self.balance >= 0 and self.overdraft_count > 0:
            self.is_active = True
            self.overdraft_count = 0
            return True
        return False

class CheckingAccount(BankAccount):
    def __init__(self, account_id: str, balance: float = 0.0):
        super().__init__(account_id, balance)
        self.account_type = "checking"

class SavingsAccount(BankAccount):
    def __init__(self, account_id: str, balance: float = 0.0):
        super().__init__(account_id, balance)
        self.account_type = "savings"

class Customer:
    def __init__(self, account_id: str, first_name: str, last_name: str, password: str):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_account: Optional[CheckingAccount] = None
        self.savings_account: Optional[SavingsAccount] = None

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_checking(self) -> bool:
        return self.checking_account is not None

    def has_savings(self) -> bool:
        return self.savings_account is not None

    def authenticate(self, password: str) -> bool:
        return self.password == password

    def get_account(self, account_type: str) -> Optional[BankAccount]:
        if account_type == "checking":
            return self.checking_account
        elif account_type == "savings":
            return self.savings_account
        return None

class Transaction:
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


