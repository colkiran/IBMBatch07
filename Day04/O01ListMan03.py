
values = list(range(10, 31, 10))
print(f"values :{values}")

# upack list
a, b, c  = values
print(a, b, c, sep=", ")

print("-" * 60)

values = list(range(10, 101, 10))
print(f"values :{values}")

print("-" * 60)
a, b, *c = values           # *var can store more than one value in a list
print(a, b, c, sep=", ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 60)
lst4 = [*lst1, *lst2]       # upacking list
print(f"lst4 :{lst4}")
print(len(lst4))

print("enmerate".center(60, "-"))
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)

for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(f"{letter[0]}\t{letter[1]}")

print("-" * 60)
for indx, letter in enumerate(letters):
    print(f"{indx}\t{letter}")

print("-" * 60)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 60)
for indx, lst in enumerate(mylist):
    print(f"{indx}\t{lst}")

print("-" * 60)
for idx, lst in enumerate(mylist):
    print(f"list({idx})")
    for id, l in enumerate(lst):
        print(f"\t\t{id}\t{l}")
