from bank.bank_system import BankSystem 

class BankCLI:
    # Command Line Interface (CLI) for the BankSystem.
    # Handles user input and calls BankSystem functions.
    
    def __init__(self):
         # Initialize the BankSystem and set no customer logged in
         self.system = BankSystem()
         self.current_customer = None

    def login(self):
        #Ask user for account ID and password and log them in if valid.  

        try:
            account_id = int(input("Enter account ID: "))
            password = input("Enter password")
            customer = self.system.authenticate(account_id, password)
            if customer:
                # If authentication succeeds, store the logged-in customer
                self.current_customer = customer
                print(f"Welcome {customer.full_name()}!")
                return True 
            else:
                print("Invalid credentials.")   
                return False 

        except ValueError:
            # Handle case where account ID is not a number
            print("Invalid account ID.")
            return False