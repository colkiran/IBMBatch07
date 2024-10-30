
class Product:

    def __init__(self, price):
        self.set_price(price)            # private varible

    def get_price(self):
        return self.__price

    def set_price(self, prc):
        if prc < 0:
            raise ValueError("Price cannot be less than zero...")
        else:
            self.__price = prc

    def del_price(self):
        self.__price = 0

    def __pvtMethod(self):
        print("Pvt Method called.....")

    def call_pvtMth(self):
        self.__pvtMethod()

import sys

try:
    pepsi = Product(45)
    print(pepsi.get_price())           # its a method

    pepsi.set_price(60)
    print(pepsi.get_price())

    pepsi.del_price()
    print(pepsi.get_price())

except:
    print("exception caught.....")
    print(sys.exc_info()[0])            # class name
    print(sys.exc_info()[1])            # message

print("-" * 60)
pepsi.call_pvtMth()
# (pepsi._Product__pvtMethod())