class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, first_name, last_name, int_rate, balance): 
            self.first_name = first_name
            self.last_name = last_name
            self.int_rate = int_rate
            self.balance = balance
            BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    
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
    
    @classmethod
    def all_info(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            account.display_account_info()
        




kevin = BankAccount("Kevin", "Yu", .01, 0)
john = BankAccount("John", "Doe", .01, 0)

kevin.deposit(100).deposit(100).deposit(100).withdraw(150).yield_interest().display_account_info()
john.deposit(1000).deposit(100).withdraw(150).withdraw(150).withdraw(150).withdraw(150).yield_interest().display_account_info()

BankAccount.all_info()


