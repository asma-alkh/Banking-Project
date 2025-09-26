import csv
from bank.customer import Customer
from bank.Transaction import Transaction 

class BankSystem:
    # Main banking system that handles customers, transactions,
    # deposits, withdrawals, and transfers.

    def __init__(self, bank_file="bank.csv", transaction_file="transactions.csv"):
        # Initialize system with CSV file paths and load customers
        self.bank_file = bank_file
        self.transaction_file = transaction_file
        self.customers = self.load_customers()  # Load existing customers from file
        self.transactions = []  # Store in-memory transaction history
        self.transaction_counter = 1  # Track transaction IDs

    def load_customers(self):
        """Load customers from CSV file into memory."""
        customers = {}
        try:
            with open(self.bank_file, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account_id = int(row["account_id"])
                    # Create a Customer object for each row
                    customers[account_id] = Customer(
                        account_id,
                        row["first_name"],
                        row["last_name"],
                        row["password"],
                        float(row["balance_checking"]),
                        float(row["balance_savings"])
                    )

        except FileNotFoundError:
            print("Bank file not found. Starting with empty customer list.")
        return customers

    def save_customers(self):
        """Save all customers back to the CSV file."""
        with open(self.bank_file, mode="w", newline="") as file:
            fieldnames = ["account_id", "first_name",
                          "last_name", "password",
                          "balance_checking", "balance_savings"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            # Write each customer as a row
            for cust in self.customers.values():
                writer.writerow({
                    "account_id": cust.account_id,
                    "first_name": cust.first_name,
                    "last_name": cust.last_name,
                    "password": cust.password,
                    "balance_checking": cust.checking_account.get_balance() if cust.has_checking() else 0.0,
                    "balance_savings": cust.savings_account.get_balance() if cust.has_savings() else 0.0,
                })

    def add_customer(self, first_name, last_name, password, with_checking=True, with_savings=False):
        """Add a new customer with optional checking/savings accounts."""
        new_id = max(self.customers.keys(), default=10000) + 1
        checking_balance = 0.0 if with_checking else None
        savings_balance = 0.0 if with_savings else None
        customer = Customer(new_id, first_name, last_name, password, checking_balance, savings_balance)

        self.customers[new_id] = customer
        self.save_customers()
        return customer

    def authenticate(self, account_id, password):
        """Authenticate a customer by ID and password."""
        customer = self.customers.get(account_id)
        if customer and customer.password == password:
            return customer
        return None

    def record_transaction(self, account_id, transaction_type, amount, from_acc, to_acc, balance_after):
        """Create and save a transaction record to memory and CSV."""
        t = Transaction(
            self.transaction_counter,
            account_id,
            transaction_type,
            amount,
            from_acc,
            to_acc,
            balance_after
        )

        self.transactions.append(t)
        self.transaction_counter += 1

        # Append to CSV file
        with open(self.transaction_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                t.transaction_id,
                t.account_id,
                t.transaction_type,
                t.amount,
                t.from_account,
                t.to_account,
                t.balance_after,
                t.timestamp
            ])

    def deposit(self, customer, account_type, amount):
        """Deposit money into a customer's account."""
        account = customer.get_account(account_type)
        if account and account.deposit(amount):
            self.record_transaction(
                customer.account_id,
                "deposit",
                amount,
                account_type,
                account_type,
                account.get_balance()
            )
            self.save_customers()
            return True
        return False

    def withdraw(self, customer, account_type, amount):
        """Withdraw money from a customer's account (checks overdraft)."""
        account = customer.get_account(account_type)
        if account:
            success, message = account.withdraw(amount)
            if success:
                self.record_transaction(customer.account_id, "withdraw", amount, account_type, account_type,
                                        account.get_balance())
                self.save_customers()
            return success, message
        return False, "Account not found"

    def transfer(self, from_customer, from_type, to_customer, to_type, amount):
        """Transfer money between accounts (can be between two customers)."""
        from_account = from_customer.get_account(from_type)
        to_account = to_customer.get_account(to_type)
        if not from_account or not to_account:
            return False, "One of the accounts does not exist"

        success, message = from_account.withdraw(amount)
        if not success:
            return False, message

        to_account.deposit(amount)
        self.record_transaction(
            from_customer.account_id,
            "transfer",
            amount,
            from_type,
            to_type,
            from_account.get_balance()
        )
        self.save_customers()
        return True, "Transfer successful"
 