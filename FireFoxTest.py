import time
from selenium import webdriver
import pagerduty


class PagePoller:
    def __init__(self, url):
        self.url = url
        self.createBrowser()

    def checkAvailable(self):
        addToCartButton = addButton = self.driver.find_element_by_class_name("add-to-cart-button")
        if ("btn-disabled" in addToCartButton.get_attribute("class")):
            return False
        else:
            addToCartButton.click()
            return True

    def createBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def refreshPage(self):
        self.driver.close()
        self.driver.quit()
        self.createBrowser()


textFile = open("bestbuy-links1.txt", "r")
lines = textFile.readlines()
print(lines)

pages = []
for u in lines:
    pages.append(PagePoller(u))

while True:
    toRemove = []
    for p in pages:
        if (p.checkAvailable()):
            pagerduty.sendPagerDutyAlert()
            toRemove.append(p)
        else:
            p.refreshPage()

    for p in toRemove:
        pages.remove(p)

    #time.sleep(0)



#
# #driver = webdriver.Firefox()
#
# # happy case - item is available
# #driver.get("https://www.bestbuy.com/site/nvidia-titan-rtx-24gb-gddr6-pci-express-3-0-graphics-card/6320585.p?skuId=6320585")
#
#
# #driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#


# good
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" style="padding:0 8px">
# </button>


# bad
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" style="padding: 0px 8px;">Sold Out</button>