class BankAccount:

    total_customers = 0

    def __init__(self, owner):
        self.owner = owner
        self._balance = 0.0
        BankAccount.total_customers += 1

    def deposit(self,num1):
        self._balance += int(num1)

    def withdraw(self, num2):
        self._balance -= int(num2)

    def get_total_customers(cls):
        return BankAccount.total_customers

    @property
    def balance(self):
        return self._balance
    
cust1 = BankAccount("Harry")
print(cust1.owner)
cust1.deposit(500)
cust1.withdraw(250)
print(cust1.balance)
print(cust1.total_customers)

cust2 = BankAccount("Virat")
print(BankAccount.total_customers)