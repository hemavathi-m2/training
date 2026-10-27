class Account: 
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance=amount+self.balance
        print(self.owner," deposited ",amount," --> balance ",self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsEroor(f"Insufficient funds: balance {self.balance}, requested {amount}")

        self.balance=self.balance-amount
        print(f"{self.owner} withdraw {amount} --> balance {self.balance}")

    def show(self):
        print(f"owner: {self.owner}, Balance: {self.balance}")


class InsufficientFundsEroor(Exception):
    pass

account=Account("Arun",1000)

try:
    account.deposit(500)
    account.withdraw(2000)

except InsufficientFundsEroor as e:
    print("Error: ",e)

finally:
    print("Transaction finished")


