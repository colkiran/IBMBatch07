
def outerFun():

    def innerFun():

        print("Hello World")


    return innerFun

outerFun()()        # calls the inner function directly

print("-" * 60)

inRef = outerFun()
inRef()

print("-" * 60)

x = outerFun()
x()
