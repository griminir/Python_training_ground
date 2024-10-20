class TagCloud:
    def __init__(self):
        # double __ = private
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add('python')
cloud.add('python')
cloud.add('Python')
print(cloud['python'])


class Product:
    def __init__(self, price):
        self.price = price

    # getting the price from a property
    @property
    def price(self):
        return self.__price

    # setting the price of a property
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price can not be negative')
        self.__price = value
    # both getter and setter are used to avoid it showing up as methods outside of the class


product = Product(-10)
print(product.price)
