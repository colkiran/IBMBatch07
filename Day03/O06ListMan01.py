
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.0, 10.5, 11.89, 12.3, 13+4j, 14-5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

# create
l1 = list(range(1, 6))
print(f"l1 :{l1}")


# read
print(f"l1[0] :{l1[0]}")
print(f"l1[3] :{l1[3]}")
print(f"l1[-1] :{l1[-1]}")

# loop
for i in l1:
    print(i, end=" ")
print()

for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

# update - replace, insert new values
# lists are static, we cannot increase the length of the list by adding new elements

print("-" * 60)
print(f"l1 :{l1}")

l1[2] = 300
l1[-1] = 500

print(f"l1 :{l1}")

# delete
print(f"l1 :{l1}")

del l1[1]
del l1[-1]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
