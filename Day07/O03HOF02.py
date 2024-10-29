def greet(msg):
    print(msg)

greet("Welcome")

fun_name = greet

print(greet.__name__)
print(fun_name.__name__)

fun_name("Hello")

print("-"  * 60)

def bank_flow(fnc):             # HOF
    print("-" * 60)
    print("logging in.....")
    fnc()
    print("logging out.....")
    print('-' * 60)

def deposit():
    print("Credited......")

def withDraw():
    print("Debited........")

def gift():
    print("transfer.........")


bank_flow(deposit)
bank_flow(withDraw)
bank_flow(gift)
