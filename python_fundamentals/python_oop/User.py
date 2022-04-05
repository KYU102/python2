class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_bal(self):
        print("User:", self.first_name, self.last_name, " Balance:", self.account_balance)


kevin = User("Kevin","Yu")
john = User("John","Doe")
jane = User("Jane","Doe")

kevin.make_deposit(100)
kevin.make_deposit(100)
kevin.make_deposit(100)
kevin.make_withdrawl(300)
kevin.display_user_bal()

john.make_deposit(500)
john.make_deposit(400)
john.make_withdrawl(200)
john.make_withdrawl(200)
john.display_user_bal()

jane.make_deposit(1000)
jane.make_withdrawl(200)
jane.make_withdrawl(200)
jane.make_withdrawl(200)
jane.display_user_bal()