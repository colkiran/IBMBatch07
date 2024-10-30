
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account  Ctor.....")

    @abstractmethod
    def getBalance(self):
        pass

class Savings(Account):

    def getBalance(self):
        print("Balace :#####")
    def deposit(self):
        print("Credited.......")

sav =Savings()


class Current(Account):

    def getBalance(self):
        print("Balance :######.##")
    def withdraw(self):
        print("Debited....")

cur = Current()
