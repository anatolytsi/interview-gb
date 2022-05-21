class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name}: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Laptop', 2000)
    print(product.get_parent_data())
    product.price = 1500
    print(product.get_parent_data())
