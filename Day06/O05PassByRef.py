
def fun(lst):
    print(f"lst :{lst}")
    lst.extend([6, 7, 8, 9, 10])
    print(f"After Modification :{lst}")

l1 = list(range(1, 6))
print(f"l1 before call:{l1}")

fun(l1)
print(f"l1 after call :{l1}")
