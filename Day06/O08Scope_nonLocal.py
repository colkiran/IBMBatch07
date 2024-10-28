

def ourterFun():
    gst = "Sachin"

    def innerFun():
        nonlocal gst         # only local var can be converted to nonlocal
        gst = "Sachin Tendulkar"
        print("Hello World")
        print(f"Greetings Mr.{gst}")


    innerFun()
    print(f"After :{gst}")
    

ourterFun()
