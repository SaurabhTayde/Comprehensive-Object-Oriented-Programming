# (NOTE: Refer Section_25 folder for detailed OOPS program)

# Run the following code through terminal with path as 'Python_ArditSulce' folder (not 'Section26_OOPS folder')

# Object here is bank account
class Account:

    def __init__(self, filepath):               # filepath is argument
        with open(filepath, 'r') as file:
            self.balance = int(file.read())      # 'self' is account object and 'balance' is instance variable

account = Account("Section26_OOPS//balance.txt")
print(account)  # We get the print result as <__main__.Account object at 0x7f32dc027e80>
                # above code indicates that '__main__' is module Account is class and since code is printing object we are also getting 'object at 0x7f32dc027e80' in output
                # Details of above description is given below:

# Now if we run command 'from Section26_OOPS import acc' through python ineractive shell we will get following output:
# '<Section26_OOPS.acc.Account object at 0x7fb8acbf5460>'
# In above output 'Section26_OOPS' is package. 'acc' is module. 'Account' is class and since code is printing object we are also getting 'object at 0x7fb8acbf5460' in output
# (Also, we can see that 'Section26_OOPS' is folder inside which 'acc' is a python code and in that code 'Account' is class)
