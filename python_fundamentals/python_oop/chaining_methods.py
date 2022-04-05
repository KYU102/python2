class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_bal(self):
        print("User:", self.first_name, self.last_name, " Balance:", self.account_balance)
        return self


kevin = User("Kevin","Yu")
john = User("John","Doe")
jane = User("Jane","Doe")

kevin.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(300).display_user_bal()

