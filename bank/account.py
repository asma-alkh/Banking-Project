# Importing the required libraries
from typing import Optional, Dict, Tuple
import datetime

# Definition of the basic category of the bank account
class BankAccount:
    """Base class for bank accounts""" 
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id 
        self.balance = balance     
        self.overdraft_count = 0 
        self.is_active = True 
        self.overdraft_limit = -100.0 
        self.overdraft_fee = 35.0

    def deposit(self, amount: float) -> bool:
        """Deposit money into account"""
        if amount <= 0:
            return False 
        self.balance += amount 
        return True 

    def can_withdraw(self, amount: float) -> Tuple[bool, str]:
        """Check if withdrawal is allowed"""
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
        """Withdraw money from account"""
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
        return True, "Withdrawal successful."

    def get_balance(self) -> float:
        """Get current balance"""
        return self.balance

    def reactivate_account(self) -> bool:
        """Reactivate account if brought current"""
        if self.balance >= 0 and self.overdraft_count > 0:
            self.is_active = True 
            self.overdraft_count = 0 
            return True 
        return False 


# Current Account Category (inherits from BankAccount)
class CheckingAccount(BankAccount):
    """Checking account class"""
    def __init__(self, account_id: str, balance: float = 0.0):
        super().__init__(account_id, balance)
        self.account_type = "checking"

# Savings Account Category (inherits from BankAccount)
class SavingsAccount(BankAccount):
    """Savings account class"""
    def __init__(self, account_id: str, balance: float = 0.0):
        super().__init__(account_id, balance)
        self.account_type = "savings"



if __name__ == "__main__":
    acc = CheckingAccount("12345", 200.0)     
    success, message = acc.withdraw(250)       
    print("Withdrawal result:", success, message)
    print("Final balance:", acc.get_balance())