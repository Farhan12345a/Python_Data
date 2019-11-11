class Account:

    def __init__(self,filepath):
        #intance variables
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance =  int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

#Inheritance
class Checking(Account):
    """THis class generates checking account"""

    type = "checking"
    
    #Inherit class from Account class
    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee = fee

    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee

jacks_check = Checking('jack.txt',1)
jacks_check.deposit(1000000)
jacks_check.transfer(28282928)
print(jacks_check.balance)
jacks_check.commit()

john_check = Checking('john.txt',1)
john_check.deposit(1000000)
john_check.transfer(28282928)
print(john_check.balance)
john_check.commit()

#how to use doc strings
print(john_checking.__doc__)



#
# account = Account("balance.txt")
# print(account.balance)
# account.withdraw(1234)
# print(account.balance)
# account.commit()
