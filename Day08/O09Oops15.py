
class Animal:

    def __init__(self):
        print(f"Animal Ctor.....")
        self.age = 1

    def eat(self):
        print("Animals eat")

class Bird(Animal):

    def fly(self):
        print("birds fly.....")

class Fish(Animal):

    def swim(self):
        print("fishes swim.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
dolphin = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 60)
print("isinstance(cuckoo, Bird) ", isinstance(cuckoo, Bird))
print("isinstance(cuckoo, Fish)", isinstance(cuckoo, Fish))
print("isinstance(cuckoo, Animal) ", isinstance(cuckoo, Animal))
print("isinstance(cuckoo, object)", isinstance(cuckoo, object))

print(isinstance(Bird, Animal))
print(isinstance(Bird, object))
print(isinstance(Bird, Fish))
