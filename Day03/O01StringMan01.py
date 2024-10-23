
# strings are immutable

st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0] :{st[0]}")        # strings are getting stored like a list
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 60)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

# reverse indexing
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing reverse order
print("-" * 60)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
# Strings are immutable
# st = "hello world"
# st[0] = "H"

# write a code to check if the string is a palindrome

st = "malayalam"
print("Plindrome" if st[:] == st[::-1] else "Not a Palindrome")

print("-" * 60)
print(dir(st))
