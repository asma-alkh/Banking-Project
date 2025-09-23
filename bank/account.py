class BankAccount:
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id 
        self.balance = balance 
        self.overdart_account = 0 
        self.is_active = True 
        self.overdart_limit = -100.0 
        self.overdart = 35.0

        def deposit(self, amount: float) -> bool:
            """Debosit money into account"""

            if amount <= 0

            return False 
             self.balance += amount 
             return True 

        def can_withdarw(self, amount: float) -> Tuple[bool, str]:
            """Chack if withdrawl is allowed"""

            if not self.is_active:
                return False "Account is deactibated"
            if amount <= 0:
                return False, "Invailid withdrawl amount" 
            new_balance = self.balance - amount           
