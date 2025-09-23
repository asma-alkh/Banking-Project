from typing import Optional
class Customer:
    """Customer class representing a bank customer"""

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
        is_authenticated = self.password == password
        if is_authenticated:
            print(f"Login successful for {self.full_name()}")
        else:
            print(f"Login failed for {self.full_name()}")
        return is_authenticated

    def get_account(self, account_type: str) -> Optional['BankAccount']:
        if account_type == "checking":
            return self.checking_account
        elif account_type == "savings":
            return self.savings_account
        return None

    def display_customer_info(self):
        print(f"\n=== CUSTOMER PROFILE ===")
        print(f"Name: {self.full_name()}")
        print(f"Account ID: {self.account_id}")
        print(f"Checking Account: {'Yes' if self.has_checking() else 'No'}")
        print(f"Savings Account: {'Yes' if self.has_savings() else 'No'}")
        print("=" * 30)

        if self.has_checking():
            self.checking_account.display_account_info()

        if self.has_savings():
            self.savings_account.display_account_info()