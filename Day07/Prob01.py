
# def outerFun(flag):
#
#     def innerFun1():
#         print("Innerfun1 called.....")
#
#     def innerFun2():
#         print("Innerfun2 called......")
#
#     if flag:
#         return innerFun1
#     else:
#         return innerFun2


# ref1 = outerFun(1)
# ref1()
#
# print("-" * 60)
#
# ref2 = outerFun(0)
# ref2()

print("-" * 60)

def outerFun(fnc):
    def wrapper(flag):
        def innerFun1():
            print("innerFun1")
            fnc()

        def innerFun2():
            print("innerFun2")
            fnc()

        if flag:
            return innerFun1
        else:
            return innerFun2

    return wrapper

@outerFun
def test():
    print("Test function called....")

res1 = test(1)
res1()

print("-" * 60)

res2 = test(0)
res2()