def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):

            from emojis import emojis
            res = emojis.encode(greet + " :" + sep + ": " + gname)
            print(res)

        return innerMostFun

    return innerFun


engGrt = outerFun("Welcome")

TgrengGrt = engGrt("lion")

TgrengGrt("Prabhakar")





"""

engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")

engGrtSngArw = engGrt("------->")
engGrtDblArw = engGrt("======>>")
hndGrtSngArw = hndGrt("------->")
hndGrtDblArw = hndGrt("======>>")


engGrtSngArw("Sachin")
engGrtDblArw("Rahul")

hndGrtSngArw("Virat")
hndGrtDblArw("Rohit")



"""