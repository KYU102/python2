class BankAccount:
    all_accounts = []
    def __init__(self, first_name, last_name, int_rate, balance): 
            self.first_name = first_name
            self.last_name = last_name
            self.int_rate = int_rate
            self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def display_account_info(self):
        print("User:", self.first_name, self.last_name, " Balance:", self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        return self



class User:
    def __init__(self,first_name,last_name, int_rate, balance):
        self.last_name = last_name
        self.account_balance = 0
        self.account = BankAccount(first_name, last_name, int_rate, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)

    def display_user_bal(self):
        self.account.display_account_info()
        print(self.account.display_account_info)


kevin = User("Kevin","Yu",.01,200)
kevin.account.deposit(100)

kevin.account.display_account_info()
