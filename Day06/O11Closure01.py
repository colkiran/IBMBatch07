
def outerFun():
    gst = "Sachin"

    def innerFun():

        print(f"Greetings {gst}")

    return innerFun

inref = outerFun()

inref()             # innerfun - lost the scope of outerfun
