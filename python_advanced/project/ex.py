class Product:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount
    def calcu_new_price(self):
        self.new_price = self.price - (self.price * self.discount)
        print(self.new_price)

obj1 = Product("p1", 2000, 0.1)
print(vars(obj1))
obj1.calcu_new_price()
print(vars(obj1))