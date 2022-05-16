from types import NoneType
from item import Item
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

class Mercari:

    def get_items(self, keyword, price_min = 0, price_max = 100, num_items_to_get = 100):

        

        return 

    def get_item_info(item_url = None) -> Item:

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
        date = str(soup.find('p', {'data-testid': 'ItemDetailsPosted'}).contents[0])
        details_unparsed = soup.find('div', {'class': 'Flex-ych44r-0 Space-cutht5-0 Container-sc-9aa7mx-0 ieZXaq'})
        desc = str(soup.find('p', {'data-testid': 'ItemDetailsDescription'}).contents[0])
        seller_reviews = str(soup.find('h6', {'class': 'Text__H6-uqn6ov-6 bkCKto'}).contents[0])


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
                else:
                    isLocal = False
                    isShipped = True

                if "$" in y:
                    shipping = str(y)
                    shipping = shipping.replace('$', '')
                    break
                
                # If free is found set shipping to 0
                if "Free" in y:
                    shipping = '0'

        # Parsing the details:
        # Find the code where to details begin
        details = []

        beginIndex = 0
        for i in details_unparsed:
            if "Details" in i:        # All the details are found after 
                break
                
            beginIndex += 1

        # Find the end of the details field
        endIndex = 0
        for i in details_unparsed:
            if "Description" in i:
                break
            
            endIndex += 1

        for i in range(beginIndex + 2, endIndex, 2): # Add two to the starting index to drop the "Details" html code at the beginnig of the list
            tempDetailList = re.split('>|<', str(details_unparsed.contents[i]))

            index = 0
            for y in tempDetailList: # Check for detail keywords

                if "dvJZSh" in y: # To capture descriptors for what the specific details actually mean
                    detailDesc = str(tempDetailList[index + 1])
                    index += 1
                    continue
                
                if "Text__T2-uqn6ov-9 hzIqmY" in y and "ItemDetailsPosted" not in y: # Commonality that precedes all the details and exclude the data in the details
                    index += 1
                    details.append(detailDesc + ": " + tempDetailList[index].replace("&amp;", "&"))
                index += 1

        # Check if the authenticated banner exists confirming the item is authenticated
        try:
            isAuth_unparsed = str(soup.find('p', {'class': 'Text-sc-1lvlnjo-0 Text__Text1-sc-1lvlnjo-2 AuthenticatedBanner__Description-sc-1t00nfx-1 edCEsC'}).contents[0])
            isAuth = True
        except:
            isAuth = False
        
        # Check if the item is sold
        try:
            isSoldOut_unparsed = str(soup.find('button', {'data-testid': 'SoldListing'}).contents[0])
            isSoldOut = True
        except:
            isSoldOut = False

        item = Item(name, price, shipping, condition)


        return item


mercari = Mercari
item = mercari.get_item_info("https://www.mercari.com/us/item/m79584435042/")
