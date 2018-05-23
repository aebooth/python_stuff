#bank

##BAD
##nathan_balance = 5000
##tucker_balance = 5000
##john_balance = 5000
##aliyah_balance = 5000
##ewan_balance = 5000
##boof_balance = 20

class BankAccount:
    account_number = 0
    def __init__(self,name,balance=0,interest_rate=0.1):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.account_number = BankAccount.account_number
        BankAccount.account_number = BankAccount.account_number + 1

    def deposit(self,amount):
        if amount <= 0:
            print("Amount must be positive and not zero!")
        else:
            self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount <= 0:
            print("Amount must be positive and not zero!")
            amount = 0
        elif amount > self.balance:
            if self.balance >= 35:
                print("The amount you entered caused an overdraft. You will be assessed a $35 fee.")
                amount = self.balance - 35
                self.balance = 0
            else:
                print("You have insufficient funds for this withdrawl!")
                amount = 0
        else:
            self.balance = self.balance - amount
        return amount
        


my_account = BankAccount("Booof",interest_rate=0.015)
print("balance: " + str(my_account.balance))
print("deposit: 100")
my_account.deposit(100)
print("balance: " + str(my_account.balance))
print("withdrawl: " + str(my_account.withdraw(150)))
print("balance: " + str(my_account.balance))









