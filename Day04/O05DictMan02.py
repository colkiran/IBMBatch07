
print("get".center(60, "-"))

player = {'name': 'Sacin Tendulkar', 'age': 34, 'runs': 98, 'oppn': 'Aus', 'venue': 'perth', 'year': 2003, 'country': 'Australia'}

print(f"player :{player}")

print("-" * 60)

print(f"Name :{player.get('name', 'Invalid key')}")
print(f"Oppn :{player.get('opn', 'Invalid key')}")

print("keys".center(60, "-"))

player = {'name': 'Sacin Tendulkar', 'age': 34, 'runs': 98, 'oppn': 'Aus', 'venue': 'perth', 'year': 2003, 'country': 'Australia'}

print(f"player :{player}")

print("-" * 60)

k = player.keys()
print(k)

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))

player = {'name': 'Sacin Tendulkar', 'age': 34, 'runs': 98, 'oppn': 'Aus', 'venue': 'perth', 'year': 2003, 'country': 'Australia'}

print(f"player :{player}")

print("-" * 60)

v = player.values()
print(v)

print("items".center(60, "-"))

emp = {
    'emp1' :{'empid': 102, 'name': 'Jack', 'age': 34, 'desig': 'MGR', 'dept': 'Finance', 'salary': 85000},
    'emp2' :{'empid': 222, 'name': 'Rita', 'age': 27, 'desig': 'TL', 'dept': 'MKT', 'salary': 55000},
    'emp3' :{'empid': 330, 'name': 'Kevin', 'age': 30, 'desig': 'SE', 'dept': 'IT', 'salary': 95000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for key, info in emp.items():
    print(key)
    print("-" * len(key))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)


print("fromkeys".center(60, "-"))
# convert a list into a dictionary

cities = ['blr', 'che', 'del', 'hyd', 'mum', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 21)
print(f"res2 :{res2}")

