class InsufficientFundsEroor(Exception):
    pass

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

class SavingAccount(Account):
    def __init__(self,owner,balance=0,min_balance=500):
        super().__init__(owner,balance)
        self.min_balance=min_balance

    def withdraw(self, amount):
        if self.balance -amount < self.min_balance:
            raise InsufficientFundsEroor(f"Insufficient funds: balance {self.balance}, requested {amount}")

        self.balance -= amount
        print(f"{self.owner} withdraw {amount} -> balance {self.balance}")

val = SavingAccount("Priya",1500)

try:
    val.withdraw(1200)
    
except InsufficientFundsEroor as e:
    print("Error:",e)

try:
    val.withdraw(800)
    
except InsufficientFundsEroor as e:
        print("Error:",e)

print(isinstance(val,Account))



