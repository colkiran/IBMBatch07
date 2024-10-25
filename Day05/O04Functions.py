"""
set of code which can execute as a unit
pass and receive data
modularity

functions are defined with def
"""

def greet():
    print("Greetings Mr.Sachin, Welcome to the event...")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event...")

# city is called default arg, gname is called non default arg
def greetGstCty(gname, y, city = "Mumbai", x = 100):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event....")


greet()

print("-" * 60)
greetGst("Sachin")
greetGst("Sourav")

print("-" * 60)

greetGstCty("Rohit", 10)
greetGstCty("Hardik", 20)
greetGstCty("Rahul", 30, "Bangalore")

print("-" * 60)
# keyword arguments or named arguments

def admission(name, dob, gender, cno, city, country, qlf, addr):
    print(f"Name            :{name}")
    print(f"DOB             :{dob}")
    print(f"Gender          :{gender}")
    print(f"Contact No      :{cno}")
    print(f"City            :{city}")
    print(f"Country         :{country}")
    print(f"Qualification   :{qlf}")
    print(f"Address         :{addr}")

# normal call
admission('Mike Tyson', '12/9/1960', 'male', '923842384', 'California', 'USA', '10th', '8th Lane, First Phase, CA')

print("-" * 60)
# keyword arguments
admission(city='LA', qlf='Graduate', gender='male', name='Richard', dob="24/03/1969", country='USA', cno='28334234', addr='No 120, 5th Cross, First Floor, aston villa')

print("-" * 60)
# return

def multiplyMe(x, y):
    return x * y

a = 10
b = 5

print(f"The product of {a} and {b} is {multiplyMe(a, b)}")

print("-" * 60)
# variable length arguments - *args, **kwargs

def prodAll(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def extract_details(**detail):
    print(detail)
    for k, v in detail.items():
        print(k, "=>", v)


extract_details(name='Rahul', age=29, runs=80, oponent="SA")

print("-" * 60)

# python supports recursive calls
# using recursive calls find
# a. factorial of a number    b. fibonacci series

print("-" * 60)

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = ArithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)      # doc string

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------
    a. if x and y are numbers then we get the sum of the numbers
    b. if x and y are strings then we get a concatinated string
    c. if x and y are different data types then it throws and error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))
# print(fun1(10, "hello"))

print("-" * 60)
help(fun1)
