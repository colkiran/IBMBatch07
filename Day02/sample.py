def fun():
    # function code
    for i in range(1, 31):
        # for loop code
        if i % 3 == 0:
            # if condition code
            print(i)
        # for loop code
        print(f"world :{i}")  # will get printed 30
    # function code
    print("hello")  # will get printed once


fun()

# --------------------------
print("-" * 60)
x = 10
# f string or format string used for interpolation
print(f"The value of x is : {x}")


