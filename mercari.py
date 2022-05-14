from item import Item
from bs4 import BeautifulSoup

newItem = Item("shoes", 15, 7, "Good", "Adidas", ["shoes", "women", "athletic shoes"], ["Size: 8.5(39)", "Model: Other"], "White Pharrell Williams shoes. Boys size 6.5")

print(newItem.__str__());

class Mercari:

    def get_items(self, keyword, price_min = 0, price_max = 100, num_items_to_get = 100):

        return 