
"""
int
float
complex
"""

a = 10
b = -10

print(f"a :{a}")
print(type(a))          # RTTI = Runtime Type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.0
d = -10.0

print(f"c: {c}")
print(type(c))
print(f"d: {d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3
print(f"e: {e}")
print(type(e))
print(f"f: {f}")
print(type(f))

print("-" * 60)
g = 3.14j
h = -3.14j
print(f"g :{g}")
print(type(g))
print(f"h: {h}")
print(type(h))

print("-" * 60)
print(10, 15, 9, 12, 14)
print(max(10, 15, 9, 12, 14))
print(min(10, 15, 9, 12, 14))

print("-" * 60)
x = 2 + 3.5
print(f"{x} \t {type(x)}")

x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary - 1 * 2 ** 2 + 0 * 2 ** 1 + 1 * 2 ** 0
print(0o11)         # octal
print(0o111)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number system conversion".center(60, "-"))
a = 100
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
