
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.age  = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):         # overload parent class constructor
        super().__init__()      # calls the parent class ctor
        print("Bird Ctor....")
        self.weight= '1 k'

    def fly(self):
        print("Birds fly.....")

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

print("-" * 60)
print(cuckoo.__dict__)