class customer:
    """Customer class representing a bank customer"""

    def __init__(self, account_id str, self.first_name, last_name: str, password: str):
        self.account_id = account_id 
        self.first_name = first_name 
        self.last_name = last_name
        self.password = password 
        self.checking_account: Optional[CheckingAccount] = None 
        self.savings_account: Optional[SavingsAccount] = None
