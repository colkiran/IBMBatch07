
print("Arithmetic Operators".center(60, "-"))
print(f"Add 10 + 3 = {10 + 3}")
print(f"Sub 10 - 3 = {10 - 3}")
print(f"Mul 10 * 3 = {10 * 3}")
print(f"Div 10 / 3 = {10 / 3}")
print(f"Flr Div 10 // 3 = {10 // 3}")
print(f"Mod 10 % 3 = {10 % 3}")
print(f"Exp 10 ** 3 = {10 ** 3}")

print("Augmentor".center(60, "-"))
# =, +=, -=, *=, /=
x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(60, "-"))
# ==, !=, >, >=, <, <=
a = 10
b = 15
print(f"a = {a}, b = {b}")
print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operator".center(60, "-"))
# and, or, not
print(f"1 == 1 and 2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and 2 == 1 :{1 == 1 and 2 == 1}")
print(f"1 == 2 and 2 == 1 :{1 == 2 and 2 == 1}")

print("-" * 60)
print(f"1 == 1 or 2 == 2 :{1 == 1 or 2 == 2}")
print(f"1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 or 2 == 2) :{not(1 == 1 or 2 == 2)}")
print(f"not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
# integer representation of unicode characters
print(f"ord('a') :{ord('a')}")      # ascii value
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print(f"chr(97) :{chr(97)}")
print(f"chr(122) :{chr(122)}")
print(f"chr(65) :{chr(65)}")
print(f"chr(90) :{chr(90)}")

print("Bitwise Operator".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print("Ternary Operator".center(60,"-"))
frt1 = "Apple"
frt2 = "Orange"
print(f"{frt1} is costlier than {frt2}")
prc = 385
wgt = 4
print(f"{frt1} is {prc} per kg and we get a discount of 20% if we buy more than 3 kgs {prc * wgt * 0.8 if wgt >= 3 else prc * wgt }")








