class BankAccount: 
    def __init__(self, account_id, first_namme, last_name, password, balance_checking=0, balance_saving=0):
        self.account_id = account_id 
        self.first_namme = first_namme 
        self.last_name = last_name 
        self.password = password
        self.balance_checking= balance_checking
        self.balance_saving = balance_saving