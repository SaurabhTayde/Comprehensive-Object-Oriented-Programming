# Inheritance:

# Inheritance is the process of creating a new class out of base class. This new class is called as subclass. And original one will be the base class
# So new class has all the properties on the methods of a base class. But also it has some other methods
# In Inheritance we can add our own instance variables for our subclass


# Base class:

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


# Sub class:

class Checking(Account):  # Note here that we are passing an argument in the subclass and this argument is nothing but the name of the base class
                          # So this is how subclass is defined by giving base class as an argument
    """ This class generates checking account object """ # This is docstring

    type = 'checking'     # This is a class variable. Class variables are declared outside the methods of that class
                          # And class variables are shared by all the instances of a class
                          # And instance variables are shared by only a particular object instance
                          # Class variables are rarely used
                          # Data Member : Instance variable and class variable both are also referred as data members
                          # Attribute : When we access instance variables or even class variables we can say we are accessing attributes of our class instance


    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# 'Instantiatation' is nothing but process of creating object instances of a class

checking = Checking("Section26_OOPS//balance.txt", 1)  # This is instantiation of the class
checking.transfer(100)
#checking.deposit(300)
print(checking.balance)
checking.commit()


# Following example will help to understand difference between class variable and instance variables:

jacks_checking = Checking("Section26_OOPS//jack.txt", 1)
jacks_checking.transfer(100)
print(jacks_checking.balance)   # Instace variable
jacks_checking.commit()
print(jacks_checking.type)      # class variable

# Following example will help to understand difference between class variable and instance variables:

johns_checking = Checking("Section26_OOPS//john.txt", 1)
johns_checking.transfer(100)
print(johns_checking.balance)  # Instace variable
johns_checking.commit()
print(johns_checking.type)     # class variable


# So, in jack and john's example here, we are getting different values for instance variables but getting same value for class variables

# Docstring print:

print(johns_checking.__doc__)
