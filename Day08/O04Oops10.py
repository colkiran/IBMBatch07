
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJs']


    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val


emp1 = Employee("Kevin", 65000)
print(emp1)

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
emp1.append('Python')

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
st = emp1[2]
print(f"st :{st}")

print("-" * 60)
emp1[2] = 'JSP'
print([e for e in emp1])
