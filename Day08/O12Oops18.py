
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.a = 1

    def eat(self):
        print("Animals eat....")


    def fun(self):
        print("Animal's function fun....")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def talk(self):
        print("Person talks......")


    def fun(self):
        print("Person's function fun....")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()      # parent class
        Person.__init__(self)
        print("Girl Ctor....")
        self.g = 30

    def walk(self):
        print("Girls walk....")

grace = Girl()
grace.eat()
grace.talk()
grace.walk()

print("-" * 60)
grace.fun()

print("-" * 60)
print(grace.__dict__)
