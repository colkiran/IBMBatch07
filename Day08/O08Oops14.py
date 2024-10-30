
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print('getter called...')
        return self.__price

    @price.setter
    def price(self, prc):
        print("setter called....")
        self.__price = prc

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.__price = 0

sprite = Product(95)
print(sprite.price)

sprite.price = 75
print(sprite.price)

del sprite.price
print(sprite.price)