
# conversions
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 367656734))
print("The number {num:2} {num:f} {num:b}".format(num = 367656734))

print("-" * 60)
print("{num:15} Tendulkar".format(num = 50))
print("{num:15} Tendulkar".format(num = "Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 60)
from math import pi
print("{}".format(pi))
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))
print("{pi:10.6}".format(pi=pi))

print("-" * 60)
print('one googol is {}'.format(10**100))
print('one googol is {:,}'.format(10**100))

print("-" * 60)
print("{pi:10.3}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("-" * 60)
print("{}".format("Sachin Tendulkar"))
print("{:>15} Tendulkar".format("Sachin"))       # right align
print("{:^15} Tendulkar".format("Sachin"))       # center align
print("{:<15} Tendulkar".format("Sachin"))       # left align

print("-" * 60)
print("{:-^60}".format("Sachin Tendulkar"))
print("Sachin Tendulkar".center(60, "-"))

print("-" * 60)
print("{1:10.4}\t{0:>10.5}".format("Sachin", "Tendulkar"))


