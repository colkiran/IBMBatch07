
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 29)
ply2.get_details()

print("-" * 60)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 60)
ply2.runs = 150

print(ply1.__dict__)
print(ply2.__dict__)
