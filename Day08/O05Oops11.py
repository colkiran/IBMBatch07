
class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJs']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(v) for v in self.tech])

emp1 = Employee("Ben")
print(emp1)

print("-" * 60)
emp1._Employee__name = "Steve"

# print(emp1.__name)
print("-" * 60)
print(emp1.__dict__)

print("-" * 60)
print(emp1)
