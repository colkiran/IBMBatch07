
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"


    def __add__(self, other):
        return Employee("noName", self.salary + other.salary)


    def __sub__(self, other):
        return Employee("noName", self.salary - other.salary)


    def __mul__(self, other):
        return Employee("noName", self.salary * other.salary)


    def __truediv__(self, other):
        return Employee("noName", self.salary / other.salary)


    def __floordiv__(self, other):
        return Employee("noName", self.salary // other.salary)


    def __mod__(self, other):
        return Employee("noName", self.salary % other.salary)


emp1 = Employee("John", 5000)
print(emp1)

print("-" * 60)
emp2 = Employee("David", 2200)
print(emp2)

print("-" * 60)
print(f"Add :{emp1 + emp2}")
print(f"Sub :{emp1 - emp2}")
print(f"Mul :{emp1 * emp2}")
print(f"Div :{emp1 / emp2}")
print(f"FlrDiv :{emp1 // emp2}")
print(f"Mod :{emp1 % emp2}")


emp3 = Employee("Aliyah", 1800)
emp4 = Employee("Tina", 3000)

res = emp1 + emp2 + emp3 + emp4
print(res)



