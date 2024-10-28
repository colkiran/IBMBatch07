
from functools import reduce
l1 = [8, 5, 3, 9, 7, 10, 4, 6]
print(f"l1 :{l1}")

res = reduce(lambda x, y : x if x > y else y, l1)
print(res)

res = reduce(lambda x, y : x if x < y else y, l1)
print(res)

print("-" * 60)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")