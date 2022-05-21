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

    def get_info(self):
        raise NotImplementedError()


class ItemDiscountReportInfoName(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportInfoPrice(ItemDiscount):
    def get_info(self):
        print(self.price)


if __name__ == '__main__':
    product_name_reporter = ItemDiscountReportInfoName('Laptop', 2000)
    product_price_reporter = ItemDiscountReportInfoPrice('Laptop', 2000)

    product_name_reporter.get_info()
    product_price_reporter.get_info()
