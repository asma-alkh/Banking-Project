from bank.bank_system import BankSystem 

class BankCLI:
    # Command Line Interface (CLI) for the BankSystem.
    # Handles user input and calls BankSystem functions.
    
    def __init__(self):
         # Initialize the BankSystem and set no customer logged in
         self.system = BankSystem()
         self.current_customer = None

    def show_menu(self):
        print("\n=== Main Menu ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Check Balance")
        print("6. Logout")
        print("7. Exit")
     

    def login(self):
        #Ask user for account ID and password and log them in if valid.  

        try:
            account_id = int(input("Enter account ID: "))
            password = input("Enter password: ")
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

    def run(self):
        print("=== Welcome to My Bank === ")
        while True:
            if not self.current_customer:
                self.show_menu()
                choice = input("Select option: ")
                
                if choice == "1":
                    self.create_account_flow()
                    continue
                elif choice == "7":
                    print("Goodbye!")
                    break
                else:
                    if not self.login():
                        continue
            else:
                self.show_menu()
                choice = input("Select option: ")
                
                if choice == "1":
                    self.create_account_flow()
                elif choice == "2":
                    self.deposit_flow()
                elif choice == "3":
                    self.withdraw_flow()
                elif choice == "4":
                    self.transfer_flow()
                elif choice == "5":
                    self.check_balance()
                elif choice == "6":
                    self.current_customer = None
                    print("Logged out")
                elif choice == "7":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")


    def create_account_flow(self):
        print("\n=== Create a New Account ===")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        password = input("Enter password: ")
        with_checking = input("Open checking account? (yes/no): ").strip().lower() == "yes"
        with_savings = input("Open savings account? (yes/no): ").strip().lower() == "yes"
        new_customer = self.system.add_customer(
        first_name, last_name, password, with_checking, with_savings
        )
        print(f"Account created successfully!")
        print(f"Your new Account ID is: {new_customer.account_id}")
        print("You can now log in using this Account ID.")
              
    def deposit_flow(self):
        # Handle the deposit process (ask for account and amount
        acc_type = input("Deposit into (checking/savings): ").lower()
        amount = float(input("Enter amount: "))
        if self.system.deposit(self.current_customer, acc_type, amount):
            print("Deposit successful.")
        else:
            print("Deposit failed. ")

    def withdraw_flow(self):
        # Handle the withdrawal process.
        acc_type = input("Withdraw from (checking/savings): ").lower()
        amount = float(input("Enter amount: "))
        success, message = self.system.withdraw(self.current_customer, acc_type, amount)
        print(message)

    def transfer_flow(self):
        # Handle money transfer between accounts/customers.
        try:
            to_id = int(input("Enter destination account ID: "))
        except ValueError:
            print("Invalid account ID.")
            return

        to_customer = self.system.customers.get(to_id)
        if not to_customer:
            print("Destination account not found.")
            return

        from_type = input("Transfer from (checking/savings): ").lower()
        to_type = input("Transfer to (checking/savings): ").lower()

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount.")
            return

        success, message = self.system.transfer(
            self.current_customer, from_type, to_customer, to_type, amount
        )
        print(message)

    def check_balance(self):
         # Display checking/savings balance for the current customer. 
        if self.current_customer.has_checking():
            print(f"Checking balance: {self.current_customer.checking_account.get_balance()}")
        if self.current_customer.has_savings():
            print(f"Savings balance: {self.current_customer.savings_account.get_balance()}")   

if __name__ == "__main__":
    app = BankCLI()
    app.run()