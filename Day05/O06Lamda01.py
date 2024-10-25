
def add(x, y):
    return x + y

a = add
res = a(20, 50)
print(res)

print("-" * 60)
# lambda var1, var2, var3....: expression - lambda will return the result of the expression

b = lambda x, y: x + y
res  = b(34, 82)
print(res)