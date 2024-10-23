
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")
print(type(l1))

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10 ,11, 12, 13, 14])

print(f"l1 :{l1}")
# print 11, 12, 13 from l1

print(l1[-1][2:5])

print("extend".center(60, "-"))
l1 = list(range(5, 11))
print(f"l1 :{l1}")

l1.extend([11, 12, 13])
l1.extend([14, 15, 16])

print(f"l1 :{l1}")
l1.extend([17])

print(f"l1 :{l1}")

print("insert".center(60, "-"))
l1 = list(range(1, 6))
print(F"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)
print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))

print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop(1)
print(f"res :{res}")

res = l1.pop()                  # removes the last element
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 1, 1, 1, 1, 2, 3, 1,1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2 ,2, 2, 2, 2, 1, 2, 3, 2, 2, 1, 1, 1, 2, 1]

l1.remove(3)
l1.remove(3)
l1.remove(3)

print(f"l1 :{l1}")

print("clear".center(60, "-"))

l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
