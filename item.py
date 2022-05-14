
from xml.sax import default_parser_list


class Item:

    def __init__(self, title, price, shipping, condition = None, brand = None, catagories = None, details = None, desc = None, isLocal = False, isAuth = False, isSoldOut = False):

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
        return f'(name={self.title}, price={self.price}, shipping={self.shipping}, condition={self.condition}, brand={self.brand}, ' \
            f'catagories={self.catagories}, details={self.details}, desc={self.desc}, isLocal={self.isLocal}, isAuth={self.isAuth}, ' \
                f'isSoldOut={self.isSoldOut})'
