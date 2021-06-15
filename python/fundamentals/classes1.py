class user:
    def __init__(self):
        self.amount = 0
        print("Hello, do you want to deposit, withdraw, transfer, or check balance?")
        
    def make_deposit(self, amount):
        deposit = float(input("Enter the amount to deposit: "))
        amount += deposit
        print("Amount deposited: " + str(deposit) + "\nCurrent amount: " + str(amount))

    def make_withdrawal(self,amount):
        withdraw = float(input("Enter the amount to deposit: "))
        amount += withdraw
        print("Amount withdrawn: " + str(withdraw) + "\nCurrent amount: " + str(amount))


    def display_user_balance(self, amount):
        print(amount)

s = user()
s.make_deposit(100)
s.make_withdrawal(500)
s.display_user_balance()
        