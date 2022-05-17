
from xml.sax import default_parser_list


class Item:

    def __init__(self, title, price, shipping, condition = None, date = None, seller_reviews = 0, brand = None, catagories = None, details = None, desc = None, isLocal = False, isAuth = False, isSoldOut = False, isShipped = True):

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
        self.date = date
        self.seller_reviews = seller_reviews
        self.isShipped = isShipped

    def __str__(self):
        return f'(name={self.title}, price={self.price}, shipping={self.shipping}, condition={self.condition}, brand={self.brand}, ' \
            f'catagories={self.catagories}, details={self.details}, desc={self.desc}, isLocal={self.isLocal}, isAuth={self.isAuth}, ' \
                f'isSoldOut={self.isSoldOut})'

    def display(self):

        print(f'\n======({self.title})======')
        print(f'Price: ${self.price} \nShipping: ${self.shipping}\nCondition: {self.condition} \nBrand: {self.brand} \n' \
            f'Catagories: {self.catagories}\nDetails: {self.details}\nDate: {self.date}\nDescription: {self.desc[0:25]}...\nAuthenticated: {self.isAuth}\n' \
                f'Sold Out: {self.isSoldOut}\nReviews: {self.seller_reviews}\n')
                
        return None

