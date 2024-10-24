
print("setdefault".center(60, "-"))

player = {'name': 'rahul', 'age': 32, 'runs': 63, 'oppn': 'zim'}
print(f"player :{player}")

# will olny add new values into the dictionary

player.setdefault('name', 'Tendulkar')
player.setdefault('age', 36 )
player.setdefault('venue', 'chepauk')
player.setdefault('year', 2005)

print(f"player :{player}")

print("-" * 60)
counts = {}
words = ['apple', 'banana', 'apple', 'cherry']

for word in words:
    counts.setdefault(word, 0)
    counts[word] += 1

print(counts)

print("pop".center(60, "-"))

player = {'name': 'rahul', 'age': 32, 'runs': 63, 'oppn': 'zim'}
print(f"player :{player}")

print("-" * 60)
res = player.pop('age')
print(f"res :{res}")

res = player.pop('runs')
print(f"res :{res}")

print("-" * 60)
res = player.pop('oppn')
print(f"plyer :{player}")

print("-" * 60)
# res = player.pop()
# print(res)

print("Popitem".center(60, "-"))
player = {'name': 'Sacin Tendulkar', 'age': 34, 'runs': 98, 'oppn': 'Aus', 'venue': 'perth', 'year': 2003, 'country': 'Australia'}

print(f"player :{player}")

print("-" * 60)

res = player.popitem()
print(f"res :{res}")
res = player.popitem()
print(f"res :{res}")
res = player.popitem()
print(f"res :{res}")


print(f"player :{player}")

print("update".center(60, "-"))

emp1 = {'empid': 102, 'name': 'Jack', 'age': 34, 'desig': 'MGR', 'salary': 85000}

emp2 = {'empid': 222, 'name': 'Rita', 'age': 27, 'desig': 'TL', 'dept': 'MKT'}

# update the values from emp2 to emp1

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)

print(f"emp1 :{emp1}")
