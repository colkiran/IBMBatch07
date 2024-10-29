
def fun(*args):
    print(args)
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)

print("-" * 60)

def sum(x, y):
    return(x + y)

def diff(x, y):
    return x - y

def log_details(fnc):               # function as an arg
    log_info = "Logging into the server....."

    def innerFun(*args):
        print(log_info)
        print(fnc(*args))
        print("-" * 60)

    return innerFun


sum_logger = log_details(sum)
sum_logger(48, 69)

print("-" * 60)

diff_logger = log_details(diff)
diff_logger(82, 49)


