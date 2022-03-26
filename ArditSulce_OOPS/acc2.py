# Object here is bank account

class Account:

    def __init__(self, filepath):                # filepath is argument
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())      # 'self' is account object and 'balance' is instance variable

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

account = Account("Section26_OOPS//balance.txt")    # Here we created object instance
print('Account Balance is: Rs. ', account.balance)

account.withdraw(100)
print('Account Balance after withdrawal is: Rs.',account.balance)

account.deposit(100)
print('Account Balance after deposit is: Rs.',account.balance)

account.commit()
