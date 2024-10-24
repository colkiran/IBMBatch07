
print("count".center(60, "-"))
l1 = [1, 2, 1, 1, 1, 1, 2, 3, 1, 1,1 , 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1,2, 3,1 , 1,1 , 1,1, 2,2, 2, 2 ,2 ,2 ,2 ]

print(f"l1 :{l1}")

print(f"count of 1 :{l1.count(1)}")
print(f"count of 2 :{l1.count(2)}")
print(f"count of 3 :{l1.count(3)}")
print(f"count of 5 :{l1.count(5)}")

print("index".center(60, "-"))

l1 = [1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1 , 1, 1, 2, 2, 2, 2, 2, 2 ,2 ]

print(f"l1 :{l1}")

print("-" * 60)
print(f"index of 1st 3 :{l1.index(3)}")

print("-" * 60)
print(f"index of 2nd 3 :{l1.index(3, l1.index(3) + 1)}")

print("-" * 60)
print(f"index of 3rd 3 :{l1.index(3, l1.index(3, l1.index(3) + 1) + 1)}")

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy list l1 to l2
l2 = l1             # shallow copy - copies the address along with data

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print('=' * 60)
print('=' * 60)

l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy l3 to l4
l4 = l3.copy()              # deep copy - only the data gets copied

print(f"l4 before :{l4}")

l4.extend([11, 12, 13])

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print('=' * 60)
print('=' * 60)

l5 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()

print(f"l6 before :{l6}")

l6[3].append(60)
l6[3].append(70)
l6[3].append(80)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print('=' * 60)
print('=' * 60)

l7 = [2, 4, [1, 3, 5, 7, 9], 6, 8, 10]
print(f"l7 :{l7}")

# copy l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)

print(f"l8 after :{l8}")

l8[2].append(11)
l8[2].append(13)
l8[2].append(15)

print(f"l8 after :{l8}")
print(F"l7 after : {l7}")