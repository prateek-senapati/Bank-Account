# COURSE: Complete Python Bootcamp: Go from zero to hero in Python 3
# INSTRUCTOR: Jose Portilla
# PLATFORM: Udemy

# Object Oriented Programming (OOP) Challenge: BANK SYSTEM

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")

my_account = Account("Prateek Senapati", 4000)
print(my_account)
my_account.deposit(1000)
print(my_account)
my_account.withdrawal(1500)
print(my_account)
my_account.withdrawal(5000)
print(my_account)
