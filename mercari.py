from item import Item
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

class Mercari:

    def get_items(self, keyword, price_min = 0, price_max = 100, num_items_to_get = 100):

        

        return 

    def get_item_info(self, item_url = None) -> Item:

        if item_url is None:
            return None


        req = Request(item_url, headers={'User-Agent': 'Mozilla/5.0'})
        source = urlopen(req).read()
        soup = BeautifulSoup(source, 'lxml')

        # Extract the important info
        name = str(soup.find('h1', {'class': 'Text__H0-uqn6ov-0 ItemInfo__Heading-ijvfho-2 kcNhNt'}).contents[0])
        price = str(soup.find('h1', {'class': 'Text__H0-uqn6ov-0 kuhXPk'}).contents[0]).replace('$', '')
        shipping_unparsed = soup.find('div', {'data-testid': 'ItemDetailsShipping'})
        condition = str(soup.find('p', {'class': 'Text__T2-uqn6ov-9 hzIqmY'}).contents[0])
        brand = str(soup.find('a', {'class': 'Spec__BrandLinkV2-sc-1n84tst-0'}).contents[0])
        catagories_unparsed = soup.find('div', {'data-testid': 'ItemDetailsCategory'})


        # Parse the catagories html code to extract the catagory keywords
        catagories = []
        for i in catagories_unparsed:
            tempCatagory = str(i)
            tempList = re.split('<|>', tempCatagory)
            
            # Grab the catagory keyword
            curCatagory = tempList[len(tempList) - 3]

            # If has '&' mercari code replace with proper character
            if "&amp;" in curCatagory:
                curCatagory = curCatagory.replace("&amp;", '&')

            catagories.append(curCatagory)
        

        shipping = ""
        # Parse the shipping string
        if len(shipping_unparsed) > 1:
            for i in shipping_unparsed:
                tempShipping = str(i)
                tempShipList = re.split('<|>|\|', tempShipping)

                for y in tempShipList:

                    # Check if item has local shipping available
                    if "Local" in y:
                        isLocal = True
            
            # Search the second shipping list for the shipping price
            # Since when both local and normal shipping options are offered
            # The shipped price is the second one to appear in the html code
            for i in tempShipList:
                if "$" in i:
                    shipping = str(i)
                    shipping = shipping.replace('$', '')
        
        # Only one shipping option available
        else:
            strShipping = str(shipping_unparsed)
            tempShipList = re.split('<|>|\|', strShipping)

            for y in tempShipList:
                
                #Check for local only
                if "Local" in y:
                    isLocal = True
                    isShipped = False

                if "$" in y:
                    shipping = str(y)
                    shipping = shipping.replace('$', '')
                    break
                
                # If free is found set shipping to 0
                if "Free" in y:
                    shipping = '0'




        print(f'\n======({name})======')
        print(f'Price: ${price} \nShipping: ${shipping}\nCondition: {condition} \nBrand: {brand} \nCatagories: {catagories}\n\n')


        return None


mercari = Mercari

mercari.get_item_info(mercari, "https://www.mercari.com/us/item/m79584435042/")


mercari.get_item_info(mercari, "https://www.mercari.com/us/item/m25195648353/")
mercari.get_item_info(mercari, "https://www.mercari.com/us/item/m93546250638/")
mercari.get_item_info(mercari, "https://www.mercari.com/us/item/m80633325507/")