from bank.account import CheckingAccount, SavingsAccount 
class Customer:

    """ Represinting a bank with Optional cheacking and savings accounts."""
    def __init__(self, account_id, first_name, last_name, password, checking_balance = 0.0, savings_balance=0.0):
         # Initialize a new customer with account ID, name, password,
        # and optional checking/savings balances.
        self.account_id =account_id
        self.first_name = first_name 
        self.last_name = last_name
        self.password = password 
        # Create accounts only if balances are provided (None means no account)
        self.checking_account = CheckingAccount(account_id, checking_balance) if checking_balance is not None else None
        self.savings_account = SavingsAccount(account_id, savings_balance) if savings_balance is not None else None

    def full_name(self):
        """Return the full name of the customer."""
        return f"{self.first_name} {self.last_name}"

    def has_checking(self):
        """Return True if the customer has a checking account."""
        return self.checking_account is not None

    def has_savings(self):
        """Return True if the customer has a savings account."""
        return self.savings_account is not None      

    def get_account(self, account_type):
        """Return the requested account ('checking'/'savings') or None if not found."""
        if account_type == "checking":
            return self.checking_account
        elif account_type == "savings":
            return self.savings_account
        return None