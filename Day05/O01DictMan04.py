
d1 = {'name': 'Rahul', 'age': '39', 'runs': 98, 'oppn': 'Aus'}
print(f"d1 before :{d1}")

# copy d1 to d2
d2 = d1         # shallow copy

print(f"d2 before :{d2}")

d2['venue'] = 'Chepauk'
d2['year'] = 2001

print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("-" * 60)
print("-" * 60)

d3 = {'name': 'Rahul', 'age': '39', 'runs': 98, 'oppn': 'Aus'}
print(f"d3 before :{d3}")

# copy d3 to d4

d4 = d3.copy()     # deep copy
print(f"d4 beore :{d4}")

d4['venue'] = 'Chepauk'
d4['year'] = 2001

print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("-" * 60)
print("-" * 60)

d5 = {'name': 'Rahul', 'age': '39', 'runs': {'aus': '98', 'eng': 70, 'wi': 85}}
print(f"d5 before :{d5}")

# copy d5 to d6

d6 = d5.copy()
print(f"d6 before :{d6}")

d6['runs']['pak'] = 120
d6['runs']['nzl'] = 65

print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

print("-" * 60)
print("-" * 60)

d7 = {'name': 'Rahul', 'age': '39', 'runs': {'aus': '98', 'eng': 70, 'wi': 85}}
print(f"d7 before :{d7}")

# copy d7 to d8
from copy import deepcopy

d8 = deepcopy(d7)

print(f"d8 before :{d8}")

d8['runs']['pak'] = 120
d8['runs']['nzl'] = 65

print(f"d8 after :{d8}")
print(f"d7 after :{d7}")
