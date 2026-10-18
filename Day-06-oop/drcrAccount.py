#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, balance, account_no):
        #  attributes  
     self.balance = balance
     self.account_no=account_no
     #debit 
    def debit(self,amount):
     self.balance-=amount
     print(f"Rs cr.{amount} ")
         #credit
    def credit(self,amount):
     self.balance+=amount
     print(f"Rs dr. {amount} ")
    def get_balance(self):
     return self.balance



account1=Account(20000,5672348)
account1.debit(1000)
account1.credit(10000)
print(account1.balance)
print(account1.account_no)
