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

    def show_menu(self):
        #Display the available banking options to the user.
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. Logout")

    def run(self):
        # Main loop for the CLI, keeps running until user exist.
        print("=== Welcome to My Bank === ")    
        while True:
            if not self.current_customer:
                # If no one is logged in, force login first
                if not self.login():
                    continue
            # Show menu and get user choice
            self.show_menu()
            choice = input("select option: ")   

            # Call corresponding function based on user choice

            if choice == "1":
                self.deposit_flow()
            elif choice == "2":
                self.withdraw_flow() 
            elif choice == "3":
                self.transfer_flow()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                # Logout the current customer
                self.current_customer = None
                print("Logged out")
            else:
                print("Invalid choice.")    

    def deposit_flow(self):
        # Handle the deposit process (ask for account and amount
        acc_type = input("Deposit into (checking/savings): ").lower()
        amount = float(input("Enter amount: "))
        if self.system.deposit(self.current_customer, acc_type, amount):
            print("Deposit successful.")
        else:
            print("Deposit failed. ")

            




