from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # will work for != also
    def __eq__(self, other):
        return self.salary == other.salary

    # will work for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee("Kevin", 55000)
emp2 = Employee("Peter", 45000)
print('-' * 60)

print(emp1)
print('-' * 60)

print(emp2)
print('-' * 60)

# compares the addresses be default
if emp1 != emp2:
    print("{}'s salary {} is NOT equal to {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is equal to {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

if emp1 < emp2:
    print("{}'s salary {} is Less than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary {} is NOT Less than {}'s salary {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


print("-" * 60)

print(emp1 >= emp2)



