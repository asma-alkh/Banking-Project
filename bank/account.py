class BankAccount:
    """Base class for bank accounts""" 
    def __init__(self, account_id: str, balance: float = 0.0):
        self.account_id = account_id 
        self.balance = balance 
        self.overdarft_account = 0 
        self.is_active = True 
        self.overdarft_limit = -100.0 
        self.overdarft = 35.0

    def deposit(self, amount: float) -> bool:
            """Debosit money into account"""

            if amount <= 0:
                return False 
            self.balance += amount 
            return True 

def can_withdarw(self, amount: float) -> Tuple[bool, str]:
    """Chack if withdrawl is allowed"""

    if not self.is_active:
        return False, "Account is deactibated"
    if amount <= 0:
        return False, "Invailid withdrawl amount" 

    new_balance = self.balance - amount

    if new_balance < self.overdarft_limit:
        return False, f"Would exced overdarft limit of {self.overdarft_limit}"  

    if self.balance < 0 and amount > 100:
        return False, "Cannot withdraw more than $100 when account is negative"
    return True, ""


    def withdraw(self, amount: float) ->Tuple[bool, str]:
            """withdraw money from account""" 
            can_withdarw, message = self.can_withdarw(amount)
            if not can_withdarw:
                return False, message 
                
                   
            would_overdarft = (self.balance - amount) < 0 and self.balance >= 0
            self.balance -= amount

            if would_overdarft:
                self.overdarft_count += 1
                self.balance -= self.ooverdarft_fee 

                if self.overdarft_count >= 2:
                    self.is_active = False 
                    return True, f"Withdrawl successful. Overdarftt fee of ${self.overdarft_fee} applied. Account deactiveated due 2 overdarfts."
                else:
                    return True, f"Withdrawl successful. Overdarft fee of ${self.overdarft_fee} applied. {2 - self.overdarft_count}overdarfts remaining befor deactivation"                        
