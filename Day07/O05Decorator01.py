
def funLogger(fnc):
    def helper(x, y):
        print("Info - Logged into the server......")
        print(fnc(x, y))
        print("Info - logged out of the server......")
        print("-" * 60)

    return helper

@funLogger
def add(x, y):
    print("add called......")
    return x + y

@funLogger
def sub(x, y):
    print("sub called.......")
    return x - y


add(34, 68)

sub(88, 54)


