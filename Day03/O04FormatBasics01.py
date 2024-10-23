
# c style printf
st = "Welcome %s, what a %s player"
val = ("Sachin", "superb")          # tuple - ()
print(st, val)

print("-" * 60)
print(st % val)

print("-" * 60)
print("Welcome %s, what a %s player" % ("Sachin", "superb"))

print("-" * 60)
print("Welcome %s, with a rating %d what a %s player" % ("Sachin", 9, "superb"))
print("Welcome %s, with a rating %d what a %s player" % ("Sachin", 9.765, "superb"))
print("Welcome %s, with a rating %.2f what a %s player" % ("Sachin", 9.765, "superb"))
print("Welcome %s, with a rating %.2f what a %s player" % ("Sachin", 9, "superb"))
print("Welcome %s, with a rating %.3f what a %s player" % ("Sachin", 9.879237409, "superb"))
print("Welcome %s, with a rating %.0f what a %s player" % ("Sachin", 9.879237409, "superb"))

print("-" * 60)
# unix style formatting
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adj="class"))

print("-" * 60)
# string format from python
print("Welcome {}, what a {} player".format("Sachin", "class"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))
print("Welcome {pname}, what a {adj} player for {ctry}".format(pname = "Sachin", adj = "class", ctry = "India"))

print("Welcome {pname}, with a rating of {rating} what a {adj} player for {ctry}".format(pname = "Sachin", rating = 9, adj = "class", ctry = "India"))

print("Welcome {pname}, with a rating of {rating:.2f} what a {adj} player for {ctry}".format(pname = "Sachin", rating = 9.73648234, adj = "class", ctry = "India"))

print("-" * 60)
# interpolation
# e - eulers constant
from math import pi, e
print(F"pi = {pi} and Eulers constant = {e}")

print("PI = {}  and Eulers Constant = {}".format(pi, e))
print("PI = {}  and Eulers Constant = {e:.3f}".format(pi, e=2.71))

print("-" * 60)
full_name = ["Sachin", "Tedulkar"]          # list
print(f"Fullname :{full_name}")
print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]}".format(name=full_name))
print("Mr.{name[1]}".format(name=full_name))
