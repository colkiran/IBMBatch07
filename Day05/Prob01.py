
def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * fact(number-1)

print(f"Factorial of a number :{fact(5)}")

"""
5 * fact(4) = 5 * 24 = 120

4 * fact(3) = 4 * 6 = 24

3 * fact(2) = 3 * 2 = 6

2 * fact(1) => 2 * 1 = 2
"""