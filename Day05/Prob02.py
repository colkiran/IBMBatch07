
def fib(number):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number-2)+fib(number-1)

print("Fibonacci of a number :")
for i in range(11):
    print(fib(i),end=" ")