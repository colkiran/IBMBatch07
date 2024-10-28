
def fun(x):         # x is a local variable
    print(f"x inside :{x}")
    greet = "Greetings Mr. Rahul"       # local variable
    print(greet)

fun(100)
print(f"x outside :{x}")
# print(f"greet outside :{greet}")