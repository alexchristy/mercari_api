
from xml.sax import default_parser_list


class Item:

    def __init__(self, title, price, shipping, isLocal, isAuth, isSoldOut, condition, brand, catagories, details, desc):

        self.isAuth = isAuth
        self.isLocal = isLocal
        self.shipping = shipping
        self.price = price
        self.title = title
        self.condition = condition
        self.brand = brand
        self.catagories = catagories
        self.details = details
        self.desc = desc
        self.isSoldOut = isSoldOut

    def __str__(self):
        return f'(name={self.title}, price={self.price}, shipping={self.shipping}, condition={self.condition}, brand={self.brand})'
