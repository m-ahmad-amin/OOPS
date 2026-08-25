class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

ahmad_account = BankAccount('Ali', 10000)

# print(ahmad_account._BankAccount__balance) # don't do this
print(ahmad_account.get_balance())

ahmad_account.deposit(1000)

print('after depositing 1000, balance: ', ahmad_account.get_balance())

ahmad_account.withdraw(2000)

print('after withdrawing 2000, balance: ', ahmad_account.get_balance())

"""
name
   
public
"Use this freely"


_name
   
internal convention
"Please don't touch this directly"


__name
   
name mangling
"Don't access this directly; Python makes accidental access harder" -> _ClassName__name
"""