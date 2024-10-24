"""
sort   - sort the original array
sorted - will take a copy of the array and sort it
"""
l1 = [9, 7, 1, 10, 8, 2, 4, 6, 3, 5]
print(f"l1 :{l1}")

# sort
res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 60)
l1 = [9, 'zebra', 7, 'yellow', 1, 'xray', 'apple',  10, 'white', 'blue', 8, 'queen', 'green', 2, 'pink', 'egg', 4, 'maroon', 'dog', 6, 'silver', 'cat', 3, 'hen', 'nib', 5, 167, 1256, 29, 276, 2519]
print(f"l1 :{l1}")

print("-" * 60)

res = sorted(l1, key=ascii)
print(f"res :{res}")

print("-" * 60)
for i in range(0, len(res)):
    # if type(res[i]) == int:
        # print(i)
    if isinstance(res[i], int):
        break

print(res[:16] + sorted(res[16:]))


print("reversed".center(60, "-"))

l1 = [9, 7, 1, 10, 8, 2, 4, 6, 3, 5]
print(f"l1 :{l1}")

# reverse and reversed
res = list(reversed(l1))
print(f"res :{res}")

print("-" * 60)
l1.reverse()
print(f"l1 :{l1}")

