class BankAccount:
    bank_name = 'ABC Bank'
    total_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        BankAccount.total_accounts += 1

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError('Amount cannot be negative')
        else: self.balance += amount

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError('Amount cannot be negative')
        elif amount > self.balance:
            raise ValueError('Balance is insufficient')
        else: self.balance -= amount

    def display_balance(self):
        print(self.balance)

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

a = BankAccount('Ali', 10000)

class SavingsAccount(BankAccount):
    total_accounts = 0

    def __init__(self, owner, balance, savings): # idk about interest, let's work with savings instead
        super().__init__(owner, balance)
        self.__savings = savings
        SavingsAccount.total_accounts += 1

    @property
    def savings(self):
        return self.__savings
    
    @savings.setter
    def savings(self, savings):
        self.__savings = savings

    def add_savings(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError('Amount cannot be negative')
        else: self.savings += amount

    def display_balance(self):
        super().display_balance()
        print(self.savings)

    # No need
    # @classmethod
    # def get_total_accounts(cls):
    #     return cls.total_accounts

class CurrentAccount(BankAccount):
    total_accounts = 0
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
        CurrentAccount.total_accounts += 1

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
            raise ValueError('Amount cannot be negative')
        elif amount > self.balance + self.overdraft_limit: # i hope it works like that but ain't sure
            raise ValueError('Balance is insufficient')
        else: self.balance -= amount

    # No need
    # @classmethod
    # def get_total_accounts(cls):
    #     return cls.total_accounts

print("\n--- TEST 1: BankAccount ---")

a = BankAccount("Ali", 10000)

print("Owner:", a.owner)
print("Balance:", a.balance)
print("Total Bank Accounts:", BankAccount.get_total_accounts())


print("\n--- TEST 2: Deposit ---")

a.deposit(2000)

print("Balance after deposit:", a.balance)


print("\n--- TEST 3: Withdraw ---")

a.withdraw(3000)

print("Balance after withdrawal:", a.balance)


print("\n--- TEST 4: SavingsAccount ---")

s = SavingsAccount("Ahmad", 5000, 1000)

print("Owner:", s.owner)
print("Balance:", s.balance)
print("Savings:", s.savings)

print("Total Bank Accounts:", BankAccount.get_total_accounts())
print("Total Savings Accounts:", SavingsAccount.get_total_accounts())


print("\n--- TEST 5: Add Savings ---")

s.add_savings(500)

print("Savings after adding:", s.savings)


print("\n--- TEST 6: CurrentAccount ---")

c = CurrentAccount("Usman", 5000, 3000)

print("Owner:", c.owner)
print("Balance:", c.balance)
print("Overdraft limit:", c.overdraft_limit)

print("Total Bank Accounts:", BankAccount.get_total_accounts())
print("Total Current Accounts:", CurrentAccount.get_total_accounts())


print("\n--- TEST 7: Overdraft ---")

c.withdraw(7000)

print("Balance after withdrawing 7000:", c.balance)


print("\n--- TEST 8: Display Balance / Overriding ---")

a.display_balance()

s.display_balance()


print("\n--- TEST 9: Invalid Deposit ---")

try:
    a.deposit(-500)
except ValueError as e:
    print("Error:", e)


print("\n--- TEST 10: Insufficient Balance ---")

try:
    a.withdraw(100000)
except ValueError as e:
    print("Error:", e)


print("\n--- TEST 11: Exceeding Overdraft ---")

try:
    c.withdraw(2000)
except ValueError as e:
    print("Error:", e)


print("\n--- FINAL COUNTS ---")

print("Bank Accounts:", BankAccount.get_total_accounts())
print("Savings Accounts:", SavingsAccount.get_total_accounts())
print("Current Accounts:", CurrentAccount.get_total_accounts())