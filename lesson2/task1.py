class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{self.name}: {self.price}'


if __name__ == '__main__':
    product = ItemDiscountReport('Laptop', 2000)
    print(product.get_parent_data())
