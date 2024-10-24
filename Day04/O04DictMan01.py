
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)

d2 = {'name': 'sachin', 'runs': 120, 'oppn': 'WI', 'venue': 'sabina park'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict(name = 'rahul', age = 28, runs = 85, oppn = 'Eng', venue = "lords")
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict([("name", 'virat'), ('age', 23), ('runs', 105), ('oppn', 'aus'), ('venue', 'gabba')])
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'Aus', 'venue': 'perth'}
print(f"player :{player}")
print(type(player))

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"Oponent :{player['oppn']}")

print("-" * 60)
# read - loop

for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# updation - modification and adding new values

print(f"player :{player}")

# modification
player['name'] = "Sacin Tendulkar"
player['runs'] = 98
player['age'] = 34

print(f"player :{player}")

# add new values
player['year'] = 2003
player['country'] = "Australia"

print(f"player :{player}")

print("-" * 60)
# delete

del player['age']
del player['country']

print(f"player :{player}")

print("-" * 60)
print(dir(player))

