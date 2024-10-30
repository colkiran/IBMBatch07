
from abc import ABC, abstractmethod

class Employee(ABC):
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job.....")


class Developer(Employee):

    def doJob(self):
        print("Developers job.....")


def Banjob(emp):
    print("Bank job started......")
    emp.doJob()
    print("Bank job completed.......")
    print("-" * 60)

mike = Manager()
david = Developer()

Banjob(mike)
Banjob(david)
