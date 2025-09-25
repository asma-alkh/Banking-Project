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
        self.checking_account = CheckingAccount(account_id, checking_balance) if checking_balance is not None else None
        self.savings.account = SavingsAccount(account_id, savings_balance) if savings_balance is not None else None


    def full_name(self):
        """ Return the. full name of the custmer. """
        return f"{self.first_name} {self.last_name}"

    def had_checking(self):
        """Return True if custmer has checking account."""
        return self.cheacking_account is not None


