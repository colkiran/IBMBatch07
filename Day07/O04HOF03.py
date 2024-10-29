
def funLogger(fnc):
    def helper():
        print("Info - Logged into the server.....")
        fnc()
        print("Info - Logged out of the server.....")
        print('=' * 60)

    return helper

def test():
    print("Function testing.....")

funLogger(test)         # no output
print("-" * 60)

funLogger(test)()
print("-" * 60)

res_fun = funLogger(test)
res_fun()
print("-" * 60)

print("-" * 60)
test = funLogger(test)
# print(test.__name__)
test()
print("-" * 60)

@funLogger              # test = funLogger(test)
def test():
    print("Function testing.....")

test()