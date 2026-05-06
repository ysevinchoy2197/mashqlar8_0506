#2-misol
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self._balance = balance
        self.__pin = pin

    def deposit(self, x):
        self._balance += x

    def withdraw(self, pin, x):
        if pin != self.__pin:
            print("Wrong pin")
        else:
            self._balance -= x

    def check_balance(self):
        print(self._balance)

acc = BankAccount("Ali", 100, 1234)

acc.deposit(50)
acc.check_balance()

acc.withdraw(1111, 50)

acc.withdraw(1234, 50)
acc.check_balance()
