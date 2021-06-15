class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance, int_rate):
        # your code here! (remember, this is where we specify the attributes for our class)
        # don't worry about user info here; we'll involve the User class soon
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self):
        # your code here
        deposit1 = float(input("Enter the amount you want to deposit: "))
        self.balance += deposit1

    def withdraw(self):
        # your code here
        withdraw1 = float(input("Enter the amount you want to withdraw: "))
        self.balance -= withdraw1

    def display_account_info(self):
        # your code here
        print("Your balance is: " + str(self.balance))

    def yield_interest(self):
        # your code here
        self.balance = self.balance + (self.balance * self.int_rate)
        print(self.balance)



bank = BankAccount(10000,0.05)
bank.deposit()
bank.withdraw()
bank.display_account_info()
# add interest
bank.yield_interest()
bank.display_account_info()
