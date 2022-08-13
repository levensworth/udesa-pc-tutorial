class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def set_max_price(self, price):
        self.__maxprice = price

    

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.set_max_price(1000)
c.sell()


class Contador:
    def __init__(self):
        self.counter = 0

    def add_item(self):
        self.counter += 1
    
    def del_item(self):
        if self.counter > 0:
            self.counter -= 1
    
    def get_counter(self) -> int:
        return self.counter

nuevo_contador = Contador()
nuevo_contador.add_item()
nuevo_contador.del_item()
print('el contador esta en ', nuevo_contador.get_counter())


