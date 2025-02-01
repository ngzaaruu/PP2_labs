class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit: {amount}. new balance: {self.balance}")
        else:
            print("deposit amount should be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"withdrawal: {amount}. new balance: {self.balance}")
        else:
            print("insufficient funds or invalid withdrawal amount.")
    
# Example usage
account = Account("Aruzhan", 1000)

account.deposit(200)   
account.withdraw(300)  
account.withdraw(1500)

