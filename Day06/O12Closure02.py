
def outerFun(greet):

    def innerFun(gname):

       print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")

# simple curry
engGrt("Sachin")
hndGrt("Sourav")