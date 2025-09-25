class BankAccount:
    """Base class for bank accounts. 
    Handles common functionality like deposit, withdraw, overdraft management, 
    and account activation/deactivation.
    """

    OVERDRAFT_LIMIT = -100.0
    OVERDRAFT_FEE = 35.0

    def __init__(self, account_id, balance=0.0):
        # Constructor: Initializes a bank account with an ID and a starting balance,
        # and sets the account as active by default.
        self.account_id = account_id
        self.balance = balance
        self.is_active = True  # Account starts as active
        self.overdraft_count = 0  # Tracks number of overdrafts

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Invalid withdrawal amount"

        if not self.is_active:
            return False, "Account is deactivated due to overdrafts"

        if self.balance < 0 and amount > 100:
            return False, "Cannot withdraw more than $100 when account is negative"

        if self.balance - amount < self.OVERDRAFT_LIMIT:
            return False, "Withdrawal denied: would exceed overdraft limit"

        self.balance -= amount

        if self.balance < 0:
            self.balance -= self.OVERDRAFT_FEE
            self.overdraft_count += 1
            if self.overdraft_count >= 2:
                self.is_active = False

        return True, "Withdrawal successful"

    def reactivate_account(self):
        if self.balance >= 0:
            self.is_active = True
            self.overdraft_count = 0
            return True
        return False


class CheckingAccount(BankAccount):
    """Represents a checking account, inherits behavior from BankAccount."""
    pass


class SavingsAccount(BankAccount):
    """Represents a savings account, inherits behavior from BankAccount."""
    pass

