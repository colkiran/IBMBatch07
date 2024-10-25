
t1 = tuple()
print(t1)
print(type(t1))

print("-" * 60)

t2 = (1, 2, 3, 4.1, 5.0, 6.5, 'seven', 'eight', 'nine', 10+2j, True)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 10, 20, 30, 40, 50
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
# tuples are immutable
# t1 = (1, 2, 3, 4, 5)
# print(f"t1 :{t1}")
#
# t1[2] = 300

# print(dir(t1))


t1 = (1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2 ,2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)

print(f"t1: {t1}")

print("count".center(60, "-"))
print(f"count of 1 :{t1.count(1)}")
print(f"count of 2 :{t1.count(2)}")
print(f"count of 3 :{t1.count(3)}")

print("index".center(60, "-"))
print(f"1st 3 :{t1.index(3)}")
print(f"2nd 3 :{t1.index(3, t1.index(3) + 1)}")
print(f"3rd 3 :{t1.index(3, t1.index(3, t1.index(3) + 1) + 1)}")

print("-" * 60)
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")
print(type(t1))

l1 = list(t1)
print(f"l1 :{l1}")
l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")

t1 = tuple(l1)
print(f"t1 :{t1}")
print(type(t1))
