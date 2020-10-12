import time

from selenium import webdriver

driver = webdriver.Firefox()

# happy case - item is available
driver.get("https://www.bestbuy.com/site/nvidia-titan-rtx-24gb-gddr6-pci-express-3-0-graphics-card/6320585.p?skuId=6320585")


# driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")

foundButton = False

while not foundButton:

    addToCartButton = addButton = driver.find_element_by_class_name("add-to-cart-button")

    if ("btn-disabled" in addToCartButton.get_attribute("class")):
        # delay or wait for some time between tries. ~3
        time.sleep(3)

        # refresh the page
        driver.refresh()

    else:
        foundButton = True



addToCartButton.click()


# good
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" style="padding:0 8px">
# </button>


# bad
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" style="padding: 0px 8px;">Sold Out</button>