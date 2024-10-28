# numbers are builtin data type which is immutable

def fun(x):
    print(f"x inside :{x}")
    x += 10
    print(f"After Modification :{x}")

y = 100
print(f"y before the call :{y}")

fun(y)
print(f"y after the call :{y}")
